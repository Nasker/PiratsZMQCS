""" GUI for the Example module

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2021'
__date__ = '14/6/21'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

import os
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QIcon, QFont
from simplecs_gui.system.logger import get_logger
from simplecs_gui.ui.modules.module import Module

from simplecs_gui.ui.modules.modpiratstemp.modpiratstemp_big_ui import Ui_ModulePiratsTempBig

import datetime
from functools import reduce

log = get_logger('modpiratstemp_gui')


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


class ModPiratsTempBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._events = EventCounter()
        self. _plot = None
        self._setup_ui()
        self._default_label_style_sheet = self._ui.lbl_set_channel_recvd.styleSheet()

    def _set_channel(self):
        value = self._ui.ledit_channel_set.text()
        ret_val = self._parent.backend.comm_client.modpiratstemp.set_temp_channel(value)
        log.debug(f"Received answer for  command: '{ret_val.as_dict}'")
        if ret_val.error:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_channel_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_channel_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_channel_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _recvd_temp(self, async_msg):
        # retrieve data
        temp = async_msg.value.get('current_temp', 0)
        # write to label
        self._ui.lbl_last_temp.setText(f"{temp:.3f}")
        # add value to events and clean them (to make sure only retain 1 minute of data)
        self._events.new_event(temp)

        self._ui.lbl_avg_minute.setText(f"{self._events.avg:.4f}")
        self._ui.lbl_events_minute.setText(f"{self._events.len}")
        x, y = self._events.averages_chart_data
        log.debug(f"widget id in _recvd_temp: {id(self)}")
        log.debug(f"self._plot type: {type(self._plot)}")
        self._plot.setData(x=x, y=y)

    def _setup_ui(self):
        self._ui = Ui_ModulePiratsTempBig()
        self._ui.setupUi(self)

        robotomono15 = QFont("Roboto", 15)
        robotomono25 = QFont("Roboto", 25)
        self._ui.lbl_avg_minute.setFont(robotomono15)
        self._ui.lbl_events_minute.setFont(robotomono15)
        self._ui.lbl_last_temp.setFont(robotomono25)

        # Add chart
        self._plot = self._ui.chart.plot()
        log.debug(f"self._ui.chart type: {type(self._ui.chart)}")
        log.debug(f"self._plot type: {type(self._plot)}")
        log.debug(f"widget id in setup_ui: {id(self)}")
        self._plot.setPen((200, 200, 100))

        self._ui.pb_channel_set.clicked.connect(self._set_channel)
        self._parent.backend.signaler.sign_be_comm_async_modpiratstemp_current_temp.connect(self._recvd_temp)


class ModPiratsTempModule(Module):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = None  # miniwidgets are the ones that goes to the column
        self._widget = None
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'media', 'temp_ico.png')
        action = QAction(QIcon(ico_path), "Pirats Temperature", self._parent)
        action.setStatusTip("Open Pirats Temperature widget")
        action.triggered.connect(self.show_modpiratstemp)
        # log.debug(f"dirname: {dirname}")
        # log.debug(f"icon: {ico_path}")
        # log.debug(f"icon exists: {os.path.exists(ico_path)}")
        return action

    def action_function(self):
        self._widget.show()

    @property
    def parent(self):
        return self._parent

    def show_modpiratstemp(self):
        if self._widget is None:
            self._widget = ModPiratsTempBigWidget(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()

