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

import os
import socket
import sys

from simplecssys import paths
from simplecssys import daemon
from simplecssys.startserver import start_server

from simplecs.logger import get_logger

log = get_logger('serverd')


class SimpleCSServerDaemon(daemon.Daemon):
    def run(self):

        application = start_server()

        log.info('Server initialized and started')

        # Create s file socket to receive stop petition by the daemon
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            os.remove(paths.FILE_SOCKET_PATH)
        except OSError:
            pass
        s.bind(paths.FILE_SOCKET_PATH)
        s.listen(1)
        conn, addr = s.accept()
        while 1:
            data = conn.recv(1024)
            if data == b'shutdown server':
                log.info('Received petition on daemon to stop server')
                break
        log.info('Stopping DAQ server')
        try:
            application.stop()
        except:
            log.exception('Failed to stop DAQ Server')
            conn.send(b'Server failed to stop. Check log and kill it manually if required')
        else:
            log.info('DAQ Server stopped')
            conn.send(b'Server stopped')
        finally:
            conn.close()


if __name__ == "__main__":

    daemon = SimpleCSServerDaemon(pid_file=paths.DAEMON_PID_FILE)


    def send_stop_to_daemon():
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(paths.FILE_SOCKET_PATH)
        s.send(b'shutdown server')
        data = s.recv(1024)
        s.close()
        print('Asked to stop daq server. Received: ' + repr(data))
        print('Asking to stop daemon')
        daemon.stop()


    if sys.argv[1] == 'start':
        daemon.start()
    elif sys.argv[1] == 'stop':
        send_stop_to_daemon()
    elif 'restart' == sys.argv[1]:
        send_stop_to_daemon()
        daemon.start()
