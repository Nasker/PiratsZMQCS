from PyQt5.QtWidgets import QMainWindow, QAction, QVBoxLayout, QTabWidget, QMdiArea
from PyQt5.QtCore import QSize

from simplecs_gui.ui.mainwindow_ui import Ui_MainWindow
from simplecs_gui.system.config import SimpleCSQtGUIConf
from simplecs_gui.backend.backend import Backend

from simplecs_gui.system.logger import get_logger

from simplecs_gui.ui.modules.logger_window.logger_window import LoggerWindowModule
from simplecs_gui.ui.modules.daq_connection.daq_conn_module import DaqConnModule
from simplecs_gui.ui.modules.modex.modex_module import ModExModule
from simplecs_gui.ui.modules.modpiratstemp.modepiratstemp_module import ModPiratsTempModule

log = get_logger('mainwindow')


class MainWindow(QMainWindow):
    def __init__(self, config: SimpleCSQtGUIConf,
                 backend: Backend, *args, **kwargs) -> None:
        """
        """
        self.conf = config
        super(MainWindow, self).__init__(*args, **kwargs)
        self.backend = backend
        self.backend.setup_signaler(self)
        self._setup()
        self._status = None
        self._modules = {}
        self._ui.mdiArea.setViewMode(QMdiArea.TabbedView)
        self._ui.toolBar.setIconSize(QSize(32, 32))
        self._add_log_module()
        self._add_conn_module()
        # This should be moved to a mod handler, is sooooo ugly here
        self._add_example_module()
        self._add_piratstemp_module()

    @property
    def toolbar(self):
        return self._ui.toolBar

    @property
    def minisbar(self) -> QVBoxLayout():
        return self._ui.vlayout_minis

    @property
    def central(self) -> QTabWidget:
        return self._ui.mdiArea

    def _add_log_module(self):
        mod = LoggerWindowModule(parent=self)
        mod.set_action_to_toolbar()
        log.info('Created loggerwindow')
        self._modules['log_viewer'] = mod

    def _add_conn_module(self):
        mod = DaqConnModule(parent=self)
        mod.add_miniwidget()
        self._modules['comm'] = mod
        log.info('Created DAQ connection module widget')

    def _add_example_module(self):
        mod = ModExModule(parent=self)
        mod.set_action_to_toolbar()
        log.info('Created modex action')
        self._modules['modex'] = mod

    def _add_piratstemp_module(self):
        mod = ModPiratsTempModule(parent=self)
        mod.set_action_to_toolbar()
        log.info('Created pirats temperature action')
        self._modules['modpiratstemp'] = mod

    def closeEvent(self, event):
        """
        """
        log.debug('Closing backend daq_client')
        self.backend.comm_client.close()
        for k, mod in self._modules.items():
            log.debug(f'Closing module {k}')
            mod.close()

    def _setup(self):
        """
        """
        self._setup_ui()

    def _setup_ui(self):
        """
        """
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.splitter.setSizes([200, 700])

    def _connections(self):
        """
        """
        pass
