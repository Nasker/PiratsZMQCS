from zmqcs.logs import set_root_logger
from piratscs.logger import log as baselog, get_logger
from piratscs.server.server import Server
from piratscs.server.modules.modHandler import ModHandler

from piratscs.server.modules.modPiratsTempServer import ModPiratsTemp
from piratscs.server.modules.modPiratsWeightServer import ModPiratsWeight
from piratscs.server.modules.modPiratsVoltageServer import ModPiratsVoltage
from piratscs.server.modules.modPressureSenseServer import ModPressureSense
from piratscs.server.modules.modPiratsInOutServer import ModPiratsInOut
from piratscs.server.modules.modMeasurementsServer import ModMeasurements

from piratscs.server.devices_manager.devicesManager import DevicesManager

from piratscs.config import FullConfig

set_root_logger(baselog)

log = get_logger('SimpleCSApp')


class ServerApplication(object):

    def __init__(self, config=FullConfig()):
        self._out = False
        self._config = config
        self._server = Server(app=self)
        self._mod_handler = ModHandler(app=self)
        self._devices_manager = DevicesManager()

    @property
    def conf(self):
        return self._config

    @property
    def server(self):
        return self._server

    @property
    def mod_handler(self):
        return self._mod_handler

    def initialize(self):
        log.info("Initializing piratscs server application")
        # Initialize the sockets (port and stuff)
        self._server.initialize()

        # Load modules
        # If modules require a start (e.g. to start threads, it must be done on the start
        # self._mod_handler.register_module(ModExample(app=self))
        self._mod_handler.register_module(ModPiratsTemp(app=self))
        self._mod_handler.register_module(ModPiratsWeight(app=self))
        self._mod_handler.register_module(ModPiratsVoltage(app=self))
        self._mod_handler.register_module(ModPressureSense(app=self))
        self._mod_handler.register_module(ModPiratsInOut(app=self))
        self._mod_handler.register_module(ModMeasurements(app=self))

    def start(self):
        # starts the threads of the server (both req-rep and pub-sub)
        log.info("Starting server part of piratscs application")
        self._server.start()
        self._mod_handler.initialize()
        self._mod_handler.connect_devices(self._devices_manager)

    def start_threads(self):
        log.info('Starting modules threads')
        self._mod_handler.start()

    def stop(self):
        log.info('Stopping piratscs application server')
        log.info('Stopping all modules')
        self._mod_handler.stop()

        # Finally stop the server
        log.info('Stopping zmq server')
        self._server.exit()
        self._server.join()
        log.debug(f"zmq server closed and joined threads")
