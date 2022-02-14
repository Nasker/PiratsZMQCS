#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '25/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from PyQt5.QtCore import QObject, pyqtSignal
from piratscs.client.client import Client as SimpleClient
from piratscs_gui.system.logger import get_logger
from piratscs_gui.backend.asyncs import AsyncReceiver

log = get_logger('backend')


class Signaler(QObject):
    sign_be_comm_client_connected = pyqtSignal(bool)
    sign_be_comm_async_app_cmd = pyqtSignal('PyQt_PyObject')
    # Add here any signal for the subscribed asyncs
    sign_be_comm_async_modex_random_number = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_modpiratstemp_current_temp = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_modpiratsweight_current_weight = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_modpiratsvoltage_current_voltage = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_modpressuresense_current_pressure = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_modpiratsinout_current_input_state = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_measurement_temp = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_measurement_pressure = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_measurement_weight = pyqtSignal('PyQt_PyObject')
    sign_be_comm_async_measurement_voltage = pyqtSignal('PyQt_PyObject')


    def __init__(self, parent):
        super().__init__(parent)

    def get_signal(self, name):
        if name.startswith('sign_be_'):
            return getattr(self, name)

    @property
    def keys(self):
        return [x for x in self._signals.keys()]


class Backend:
    def __init__(self, config):
        self.conf = config
        self._signaler = None
        self._comm_client = SimpleClient()
        self._comm_client_asyncs = AsyncReceiver(backend=self)
        # AsyncReceiver already register the asyncs callbacks. Until there is a valid signaler, the async callback
        # won't execute

    def setup_signaler(self, parent):
        self._signaler = Signaler(parent)

    def connect_to_server(self, ip, req_port, async_port):
        self._comm_client.connect(ip=ip, req_port=req_port, async_port=async_port)
        self._comm_client.start()
        log.debug(f"Connected to {ip}:{req_port}:{async_port}")
        self._signaler.sign_be_comm_client_connected.emit(True)

    @property
    def comm_client(self):
        return self._comm_client

    @property
    def signaler(self):
        return self._signaler

    @property
    def async_exec(self):
        return self._comm_client_asyncs

