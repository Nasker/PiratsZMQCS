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
import colorsys
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QIcon, QFont
from piratscs_gui.system.logger import get_logger
from piratscs_gui.ui.modules.module import Module

from piratscs_gui.ui.modules.modpiratsvoltage.modpiratsvoltage_big_ui import Ui_ModulePiratsVoltageBig

import datetime
from functools import reduce

log = get_logger('modpiratsvoltage_gui')

colors = ['eb3434','ebe834','5feb34','34e5eb','3459eb','9934eb','eb34d0','eb8934']

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


class ModPiratsVoltageBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        # self._events = EventCounter()
        # self._plot = None
        self._plots = []
        self._setup_ui()
        self._default_label_style_sheet = self._ui.lbl_set_channel_recvd.styleSheet()
        self._events_list = []
        self._events_list.append(EventCounter())

    def _set_channel(self):
        value = self._ui.ledit_channel_set.text()
        ret_val = self._parent.backend.comm_client.modpiratsvoltage.set_voltage_channel(value)
        created_channels = value.count(",") + 1
        log.debug(f"Received answer for  command: '{ret_val.as_dict}'")
        self._events_list.clear()
        self._events_list = [EventCounter() for _ in range(0, created_channels)]
        self._plots.clear()
        self._plots = [self._ui.chart.plot() for _ in range(0, created_channels)]
        # self._ui.chart.reset()

        if ret_val.error:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_channel_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_channel_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_channel_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _recvd_voltage(self, async_msg):
        # retrieve data
        voltage_list = async_msg.value.get('current_voltage', 0)
        log.debug(f"VOLTAGE LIST ON GUI MODULE{voltage_list}")
        # write to label
        # voltage = voltage_list[0]['1']
        voltage_shown_str =''
        for n,voltage_dict in enumerate(voltage_list):
            for key, value in voltage_dict.items():
                voltage_shown_str += (f'-CH{key}: {value:.2f} Kg   ')
                self._events_list[n].new_event(value)
                x, y = self._events_list[n].averages_chart_data
                # log.debug(f'-{n}: {y}')
                self._plots[n].setData(x=x, y=y, pen=colors[n], thickness=3)
        self._ui.lbl_last_voltage.setText(voltage_shown_str)

    def _setup_ui(self):
        self._ui = Ui_ModulePiratsVoltageBig()
        self._ui.setupUi(self)

        robotomono15 = QFont("Roboto", 15)
        self._ui.lbl_last_voltage.setFont(robotomono15)

        # Add chart
        # self._plot = self._ui.chart.plot()
        self._plots.append(self._ui.chart.plot())

        log.debug(f"self._ui.chart type: {type(self._ui.chart)}")
        log.debug(f"self._plot type: {type(self._plots[0])}")
        log.debug(f"widget id in setup_ui: {id(self)}")
        # self._plot.setPen((200, 200, 100))
        self._plots[0].setPen((200, 200, 100))

        self._ui.pb_channel_set.clicked.connect(self._set_channel)
        self._parent.backend.signaler.sign_be_comm_async_modpiratsvoltage_current_voltage.connect(self._recvd_voltage)


class ModPiratsVoltageModule(Module):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = None  # miniwidgets are the ones that goes to the column
        self._widget = None
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'media', 'voltage_ico.png')
        action = QAction(QIcon(ico_path), "Pirats Voltage", self._parent)
        action.setStatusTip("Open Pirats Voltage widget")
        action.triggered.connect(self.show_modpiratsvoltage)
        # log.debug(f"dirname: {dirname}")
        # log.debug(f"icon: {ico_path}")
        # log.debug(f"icon exists: {os.path.exists(ico_path)}")
        return action

    def action_function(self):
        self._widget.show()

    @property
    def parent(self):
        return self._parent

    def show_modpiratsvoltage(self):
        if self._widget is None:
            self._widget = ModPiratsVoltageBigWidget(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()

