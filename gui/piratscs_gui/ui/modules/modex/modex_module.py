""" GUI for the Example module

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '22/2/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import os
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QIcon, QFont
from piratscs_gui.system.logger import get_logger
from piratscs_gui.ui.modules.module import Module

from piratscs_gui.ui.modules.modex.modex_big_ui import Ui_ModuleExampleBig

import datetime
import pprint
from functools import reduce

import pyqtgraph as pg

log = get_logger('modex_gui')


class EventCounter:
    def __init__(self, interval=60):
        self._events = []
        self._interval = interval
        self._avgs = []
        self._avgs_ts = []

    def new_event(self, value):
        now = self.now
        self._events.append((value, now))
        self._clean()
        self._avgs.append(self._avg())
        self._avgs_ts.append(now)

    @property
    def now(self):
        return datetime.datetime.utcnow().timestamp()

    @property
    def threshold(self):
        return self.now - self._interval

    def _clean(self):
        th = self.threshold
        self._events = [x for x in self._events if x[1] > th]
        self._avgs_ts = [x for x in self._avgs_ts if x > th]
        self._avgs = self._avgs[-len(self._avgs_ts):]

    @property
    def avg(self):
        return self._avgs[-1]

    def _avg(self):
        lst = [x[0] for x in self._events]
        return reduce(lambda a, b: a + b, lst) / len(lst)

    @property
    def len(self):
        return len(self._events)

    @property
    def averages_chart_data(self):
        return self._avgs_ts, self._avgs


class ModexBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._events = EventCounter()
        self._plot = None
        self._setup_ui()
        self._default_label_style_sheet = self._ui.lbl_set_max_rnd_recvd.styleSheet()

    def _send_echo_cmd(self):
        value = self._ui.ledit_echo_cmd.text()
        ret_val = self._parent.backend.comm_client.modex.echo(value)
        # log.debug(f"Received answer for echo command: '{ret_val.as_dict}'")
        self._ui.lbl_echo_recvd.setText(str(ret_val.ans))
        self._ui.lbl_echo_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _set_max_rnd(self):
        value = self._ui.ledit_max_rnd.text()
        ret_val = self._parent.backend.comm_client.modex.set_max_rnd(value)
        log.debug(f"Received answer for set_max_rnd command: '{ret_val.as_dict}'")
        if ret_val.error:
            self._ui.lbl_set_max_rnd_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_max_rnd_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_max_rnd_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_max_rnd_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_max_rnd_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _recvd_random(self, async_msg):
        # retrieve data
        rnd = async_msg.value.get('random', 0)
        # write to label
        self._ui.lbl_last_random.setText(f"{rnd:.3f}")
        # add value to events and clean them (to make sure only retain 1 minute of data)
        self._events.new_event(rnd)

        self._ui.lbl_avg_minute.setText(f"{self._events.avg:.4f}")
        self._ui.lbl_events_minute.setText(f"{self._events.len}")
        x, y = self._events.averages_chart_data
        log.debug(f"widget id in _recvd_random: {id(self)}")
        log.debug(f"self._plot type: {type(self._plot)}")
        self._plot.setData(x=x, y=y)

    def _setup_ui(self):
        self._ui = Ui_ModuleExampleBig()
        self._ui.setupUi(self)

        robotomono15 = QFont("Roboto", 15)
        robotomono25 = QFont("Roboto", 25)
        self._ui.lbl_avg_minute.setFont(robotomono15)
        self._ui.lbl_events_minute.setFont(robotomono15)
        self._ui.lbl_last_random.setFont(robotomono25)

        # Add chart
        self._plot = self._ui.chart.plot()
        log.debug(f"self._ui.chart type: {type(self._ui.chart)}")
        log.debug(f"self._plot type: {type(self._plot)}")
        log.debug(f"widget id in setup_ui: {id(self)}")
        self._plot.setPen((200, 200, 100))

        self._ui.pb_echo.clicked.connect(self._send_echo_cmd)
        self._ui.pb_set_max_rnd.clicked.connect(self._set_max_rnd)
        self._parent.backend.signaler.sign_be_comm_async_modex_random_number.connect(self._recvd_random)


class ModExModule(Module):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = None  # miniwidgets are the ones that goes to the column
        self._widget = None
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'media', 'example_action_ico_64.png')
        action = QAction(QIcon(ico_path), "Show Example", self._parent)
        action.setStatusTip("Open modex widget")
        action.triggered.connect(self.show_modex)
        # log.debug(f"dirname: {dirname}")
        # log.debug(f"icon: {ico_path}")
        # log.debug(f"icon exists: {os.path.exists(ico_path)}")
        return action

    def action_function(self):
        self._widget.show()

    @property
    def parent(self):
        return self._parent

    def show_modex(self):
        if self._widget is None:
            self._widget = ModexBigWidget(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()

