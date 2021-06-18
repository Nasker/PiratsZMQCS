#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '8/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import os
if os.name != 'nt':
    import pwd
else:
    pwd = None
from pathlib import Path

if pwd:
    user = pwd.getpwuid(os.getuid())[0]
else:
    user = None

NAME = 'piratscs'

if user == 'root':
    BASE_PATH = f'/var/{NAME}/'
    LOGS_PATH = f'/var/log/{NAME}'
else:
    BASE_PATH = os.path.join(Path.home(), NAME)
    LOGS_PATH = os.path.join(BASE_PATH, 'log')

CONFIGURATION_FILE_PATH = os.path.join(BASE_PATH, 'config.json')
MAIN_LOG_FILE = os.path.join(LOGS_PATH, f'{NAME}_server.log')

DAEMON_PID_FILE = os.path.join(BASE_PATH, 'pid.file')
FILE_SOCKET_PATH = os.path.join(BASE_PATH, 'daemon.socket')

CREATE_PATHS = [
    BASE_PATH,
    LOGS_PATH,
]


def create_paths_if_not_exists():
    for p in CREATE_PATHS:
        if not os.path.exists(p):
            os.makedirs(p)


def custom_config_exists():
    return os.path.exists(CONFIGURATION_FILE_PATH)


if __name__ == "__main__":

    create_paths_if_not_exists()
    print(custom_config_exists())