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

from piratscs_gui.ui.modules.modpiratsinout.modpiratsinout_big_ui import Ui_ModulePiratsInOutBig
from piratscs_gui.ui.modules.Common.EventCounter import EventCounter
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list

N_CHANNELS = 16
N_ROWS = 2
N_COLS = int(N_CHANNELS / N_ROWS)

colors = get_colors_list(N_CHANNELS)

log = get_logger('modpiratsinout_gui')

class ModPiratsInOutBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        # self._events = EventCounter()
        # self._plot = None
        self._plots = []
        self._setup_ui()
        self._events_list = []
        self._events_list.append(EventCounter())


    def _recvd_voltage(self, async_msg):
        voltage_list = async_msg.value.get('current_voltage', 0)
        log.debug(f"VOLTAGE LIST ON GUI MODULE{voltage_list}")
        voltage_shown_str =''
        for n,voltage_dict in enumerate(voltage_list):
            for key, value in voltage_dict.items():
                voltage_shown_str += (f'-CH{key}: {value:.3f} V   ')
                self._events_list[n].new_event(value)
                x, y = self._events_list[n].averages_chart_data
                self._plots[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        # self._ui.lbl_last_voltage.setText(voltage_shown_str)

    def _setup_ui(self):
        self._ui = Ui_ModulePiratsInOutBig()
        self._ui.setupUi(self)
        for j in range (N_ROWS):
            for i in range(N_COLS):
                self.select_out_btn = QtWidgets.QPushButton(self)
                self.select_in_btn = QtWidgets.QPushButton(self)
                self.select_out_btn.setCheckable(True)
                self.select_out_btn.setObjectName(f"select_out_{i}_btn")
                self.select_in_btn.setObjectName(f"select_in_{i}_btn")
                self.select_out_btn.setText(f"OUT{i + j * N_COLS}")
                self.select_in_btn.setText(f"IN{i + j * N_COLS}")
                self.select_out_btn.setMinimumSize(120, 120)
                self.select_in_btn.setMinimumSize(120, 120)
                self._ui.outputs_gridLayout.addWidget(self.select_out_btn, j, i)
                self._ui.inputs_gridLayout.addWidget(self.select_in_btn, j , i)
                self.select_in_btn.clicked.connect(self.print_selected_in_channels_ledit)
                self.select_out_btn.clicked.connect(self.print_selected_out_channels_ledit)
        log.debug(f"widget id in setup_ui: {id(self)}")
        self._parent.backend.signaler.sign_be_comm_async_modpiratsvoltage_current_voltage.connect(self._recvd_voltage)

    def print_selected_out_channels_ledit(self):
        active_outputs = []
        for j in range (N_ROWS):
            for i in range(N_COLS):
                if self._ui.outputs_gridLayout.itemAtPosition(j, i).widget().isChecked():
                    active_outputs.append(i+j*N_COLS)
        print(f"active outputs: {active_outputs}")

    def print_selected_in_channels_ledit(self):
        active_inputs = []
        for j in range(N_ROWS):
            for i in range(N_COLS):
                if self._ui.inputs_gridLayout.itemAtPosition(j, i).widget().isChecked():
                    active_inputs.append(i + j * N_COLS)
        print(f"active inputs: {active_inputs}")

class ModPiratsInOutModule(Module):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = None  # miniwidgets are the ones that goes to the column
        self._widget = None
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'media', 'inout_ico.png')
        action = QAction(QIcon(ico_path), "Pirats InOut", self._parent)
        action.setStatusTip("Open Pirats InOut widget")
        action.triggered.connect(self.show_modpiratsinout)
        return action

    def action_function(self):
        self._widget.show()

    @property
    def parent(self):
        return self._parent

    def show_modpiratsinout(self):
        if self._widget is None:
            self._widget = ModPiratsInOutBigWidget(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()