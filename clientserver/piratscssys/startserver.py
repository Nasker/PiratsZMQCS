#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2020'
__date__ = '05/06/2020'
__credits__ = ['Otger Ballester', ]
__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from piratscs.logger import log_add_file_handler, log, log_add_stream_handler
from piratscssys import paths


def start_server(log_to_screen=False):

    paths.create_paths_if_not_exists()

    log_add_file_handler(paths.MAIN_LOG_FILE)
    if log_to_screen:
        log_add_stream_handler()
    log.info('Launching server daemon')

    from piratscs.config import FullConfig

    config = FullConfig()
    # check if there is a custom configuration file:
    if paths.custom_config_exists():
        log.info(f'Loading custom configuration file from {paths.CONFIGURATION_FILE_PATH}')
        config.load_json(paths.CONFIGURATION_FILE_PATH)

    from piratscs.application import ServerApplication

    app = ServerApplication(config=config)

    app.initialize()
    app.start()

    return app


if __name__ == "__main__":
    application = start_server(log_to_screen=True)
    import threading
    event = threading.Event()

    log.info('Server initialized and started. Waiting for events')
    try:
        print('Press Ctrl+C to exit')
        event.wait()
    except KeyboardInterrupt:
        print('wait until application stops')
        application.stop()
        print('got Ctrl+C')

