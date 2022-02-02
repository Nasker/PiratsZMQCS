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
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list

N_CHANNELS = 16
N_ROWS = 2
N_COLS = int(N_CHANNELS / N_ROWS)

colors = get_colors_list(N_CHANNELS)

log = get_logger('modpiratsinout_gui')

def int_to_bool_list(num, n_bits):
    return [bool(num & (1<<n)) for n in range(n_bits)]

class ModPiratsInOutBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._setup_ui()
        self._default_label_style_sheet = self._ui.lbl_set_channel_recvd.styleSheet()

    def _start_acq(self):
        self._parent.backend.comm_client.modpiratsinout.start_acq()
        log.debug("Started inputs state acquisition")

    def _stop_acq(self):
        self._parent.backend.comm_client.modpiratsinout.stop_acq()
        log.debug("Stopped inputs state acquisition")

    def _update_inputs_state(self, states_list):
        for j in range(N_ROWS):
            for i in range(N_COLS):
                #self._ui.inputs_gridLayout.itemAtPosition(j, i).widget().setEnabled(states_list[j*N_COLS + i])
                self._ui.inputs_gridLayout.itemAtPosition(j, i).widget().setChecked(states_list[j*N_COLS + i])

    def _recvd_input(self, async_msg):
        inputs_states_list = async_msg.value.get('current_inputs_state', 0)
        inputs_states_list = int_to_bool_list(inputs_states_list, N_CHANNELS)
        inputs_shown_str = str(inputs_states_list)
        self._ui.lbl_set_channel_recvd_on.setText(inputs_shown_str)
        self._update_inputs_state(inputs_states_list)

    def _setup_ui(self):
        self._ui = Ui_ModulePiratsInOutBig()
        self._ui.setupUi(self)
        for j in range (N_ROWS):
            for i in range(N_COLS):
                self.select_out_btn = QtWidgets.QPushButton(self)
                self.select_in_btn = QtWidgets.QPushButton(self)
                self.select_out_btn.setCheckable(True)
                self.select_in_btn.setCheckable(True)
                self.select_out_btn.setObjectName(f"select_out_{i + j * N_COLS}_btn")
                self.select_in_btn.setObjectName(f"select_in_{i + j * N_COLS}_btn")
                self.select_out_btn.setText(f"{i + j * N_COLS}")
                self.select_in_btn.setText(f"{i + j * N_COLS}")
                # self.select_out_btn.setStyleSheet(f"border-color: #{colors[i + j * N_COLS]}")
                # self.select_in_btn.setStyleSheet(f"border-color: #{colors[i + j * N_COLS]}")
                self.select_out_btn.setMinimumSize(120, 120)
                self.select_in_btn.setMinimumSize(120, 120)
                self._ui.outputs_gridLayout.addWidget(self.select_out_btn, j, i)
                self._ui.inputs_gridLayout.addWidget(self.select_in_btn, j , i)
                self.select_out_btn.clicked.connect(self.act_on_output_btn_clicked)
        log.debug(f"widget id in setup_ui: {id(self)}")
        self._ui.start_acq_btn.clicked.connect(self._start_acq)
        self._ui.stop_acq_btn.clicked.connect(self._stop_acq)
        self._parent.backend.signaler.sign_be_comm_async_modpiratsinout_current_input_state.connect(self._recvd_input)

    def act_on_output_btn_clicked(self):
        output = int(self.sender().text())
        state = self.sender().isChecked()
        ret_val = self._parent.backend.comm_client.modpiratsinout.set_output_state(output, state)
        log.debug(f"Received answer for  command: '{ret_val.as_dict}'")
        if ret_val.error:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_channel_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_channel_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_channel_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))


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