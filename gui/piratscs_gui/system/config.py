#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '26/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'


from piratscssys.config import ConfObject
from piratscs_gui.system.paths import LOGS_PATH
import os


class ServerComm(ConfObject):
    ip = 'localhost'
    cmd_port = 56485
    async_port = 56486


class Logging(ConfObject):
    save_logs = True
    log_path = os.path.join(LOGS_PATH, 'simplecs_qtgui.log')
    show_stream = True


class SimpleCSQtGUIConf(ConfObject):
    server_comm = ServerComm()
    logging = Logging()


