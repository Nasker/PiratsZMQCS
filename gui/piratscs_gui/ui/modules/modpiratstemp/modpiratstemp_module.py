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
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QIcon, QFont
from piratscs_gui.system.logger import get_logger
from piratscs_gui.ui.modules.module import Module

from piratscs_gui.ui.modules.modpiratstemp.modpiratstemp_big_ui import Ui_ModulePiratsTempBig
from piratscs_gui.ui.modules.Common.EventCounter import EventCounter
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list

log = get_logger('modpiratstemp_gui')

N_CHANNELS = 16
N_ROWS = 2
N_COLS = int(N_CHANNELS / N_ROWS)

colors = get_colors_list(N_CHANNELS)

class ModPiratsTempBigWidget(QWidget):
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
        ret_val = self._parent.backend.comm_client.modpiratstemp.set_temp_channel(value)
        created_channels = value.count(",") + 1
        log.debug(f"Received answer for  command: '{ret_val.as_dict}'")
        self._events_list.clear()
        self._events_list = [EventCounter() for _ in range(0, created_channels)]
        self._plots.clear()
        self._plots = [self._ui.chart.plot() for _ in range(0, created_channels)]
        if ret_val.error:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_channel_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_channel_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_channel_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _start_acq(self):
        self._parent.backend.comm_client.modpiratstemp.start_acq()
        log.debug("Started temperature acquisition")

    def _stop_acq(self):
        self._parent.backend.comm_client.modpiratstemp.stop_acq()
        log.debug("Stopped temperature acquisition")

    def _clear_chart(self):
        self._ui.chart.clear()

    def _recvd_temp(self, async_msg):
        temp_list = async_msg.value.get('current_temp', 0)
        log.debug(f"TEMP LIST ON GUI MODULE{temp_list}")
        temp_shown_str =''
        for n,temp_dict in enumerate(temp_list):
            for key, value in temp_dict.items():
                temp_shown_str += (f'-CH{key}: {value:.2f} ºC   ')
                self._events_list[n].new_event(value)
                x, y = self._events_list[n].averages_chart_data
                self._plots[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        self._ui.lbl_last_temp.setText(temp_shown_str)

    def _setup_ui(self):
        self._ui = Ui_ModulePiratsTempBig()
        self._ui.setupUi(self)
        for j in range (N_ROWS):
            for i in range(N_COLS):
                self.select_btn_ch = QtWidgets.QCheckBox(self)
                self.select_btn_ch.setCheckable(True)
                self.select_btn_ch.setObjectName(f"select_btn_ch{i}")
                self.select_btn_ch.setText(f"CH{i + j * N_COLS}")
                self.select_btn_ch.setStyleSheet(f"color: #{colors[i + j * N_COLS]}")
                self._ui.gridLayout.addWidget(self.select_btn_ch, j , i)
                self.select_btn_ch.clicked.connect(self.print_selected_channels_ledit)
        robotomono15 = QFont("Roboto", 15)
        self._ui.lbl_last_temp.setFont(robotomono15)
        self._plots.append(self._ui.chart.plot())
        log.debug(f"self._ui.chart type: {type(self._ui.chart)}")
        log.debug(f"self._plot type: {type(self._plots[0])}")
        log.debug(f"widget id in setup_ui: {id(self)}")
        self._plots[0].setPen((200, 200, 100))
        self._ui.pb_channel_set.clicked.connect(self._set_channel)
        self._ui.start_acq_btn.clicked.connect(self._start_acq)
        self._ui.stop_acq_btn.clicked.connect(self._stop_acq)
        self._ui.btn_clear_chart.clicked.connect(self._clear_chart)
        self._parent.backend.signaler.sign_be_comm_async_modpiratstemp_current_temp.connect(self._recvd_temp)

    def print_selected_channels_ledit(self):
        active_channels = []
        for j in range (N_ROWS):
            for i in range(N_COLS):
                if self._ui.gridLayout.itemAtPosition(j, i).widget().isChecked():
                    active_channels.append(i+j*N_COLS)
        self._ui.ledit_channel_set.setText(",".join(str(x) for x in active_channels))


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