from zmqcs.logs import set_root_logger
from simplecs.logger import log as baselog, get_logger
from simplecs.server.server import Server
from simplecs.server.modules.modHandler import ModHandler

from simplecs.server.modules.modexample import ModExample

from simplecs.config import FullConfig

set_root_logger(baselog)

log = get_logger('SimpleCSApp')


class ServerApplication(object):

    def __init__(self, config=FullConfig()):
        self._out = False
        self._config = config
        self._server = Server(app=self)
        self._mod_handler = ModHandler(app=self)

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
        log.info("Initializing simplecs server application")
        # Initialize the sockets (port and stuff)
        self._server.initialize()

        # Load modules
        # If modules require a start (e.g. to start threads, it must be done on the start
        self._mod_handler.register_module(ModExample(app=self))

    def start(self):
        # starts the threads of the server (both req-rep and pub-sub)
        log.info("Starting server part of simplecs application")
        self._server.start()
        log.info('Starting modules')
        self._mod_handler.start()

    def stop(self):

        log.info('Stopping simplecs application server')
        log.info('Stopping all modules')
        self._mod_handler.stop()

        # Finally stop the server
        log.info('Stopping zmq server')
        self._server.exit()
        self._server.join()
        log.debug(f"zmq server closed and joined threads")
