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
from PyQt5.QtGui import QIcon
from simplecs_gui.system.logger import get_logger
from simplecs_gui.ui.modules.module import Module

from simplecs_gui.ui.modules.modex.modex_big_ui import Ui_ModuleExampleBig

import datetime
import pprint

log = get_logger('modex_gui')


class ModexBigWidget(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._setup_ui()

    def _send_echo_cmd(self):
        value = self._ui.ledit_echo_cmd.text()
        ret_val = self._parent.backend.comm_client.modex.echo(value)
        # log.debug(f"Received answer for echo command: '{ret_val.as_dict}'")
        self._ui.lbl_echo_recvd.setText(str(ret_val.ans))
        self._ui.lbl_echo_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

    def _recvd_random(self, async_msg):

        self._ui.lbl_last_random.setText(f"{async_msg.value.get('random', 0):.5f}")

    def _setup_ui(self):
        self._ui = Ui_ModuleExampleBig()
        self._ui.setupUi(self)

        self._ui.pb_echo.clicked.connect(self._send_echo_cmd)

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
        log.debug(f"dirname: {dirname}")
        log.debug(f"icon: {ico_path}")
        log.debug(f"icon exists: {os.path.exists(ico_path)}")
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

