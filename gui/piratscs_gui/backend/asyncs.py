#!/usr/bin/env python
# -*- coding: utf-8 -*-
from piratscs_gui.system.logger import get_logger
from zmqcs.client.callbacks import AsyncCallback

""" A simple Aync package processer that only keeps track of all received 
"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2020'
__date__ = '27/07/2020'
__credits__ = ['Otger Ballester', ]
__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

log = get_logger('asyncs')


class AsyncStatsCB(AsyncCallback):
    """This class receives all asyncs from the server and generates some statistics"""

    def __init__(self):
        super().__init__()
        self._db = {}

    def _run(self, key, msg):
        if key not in self._db:
            self._db[key] = {'total': 0,
                             'last': None}
        self._db[key]['total'] += 1
        self._db[key]['last'] = msg

    def keys(self):
        return self._db.keys()

    def stats(self):
        return {k: self._db[k]['total'] for k in self._db}

    def last(self, key):
        """last is a zmqcs.common.message.AsyncMSG"""
        if key in self._db:
            return self._db[key]['last']
        k = key.encode('utf-8')
        if k in self._db:
            return self._db[k]['last']
        return f"key '{key}' nor '{k}' not found in DB"


class AsyncSignalerCB(AsyncCallback):
    # This callback to work requires that a Signaler has been configured on the backend.
    # Signaler must be a QObject in order to generate signals
    def __init__(self, backend):
        super().__init__()
        self._be = backend

    def _run(self, key, msg):
        # will emit a zmqcs.common.message.AsyncMSG
        if self._be.signaler is not None:
            signal = self._be.signaler.get_signal(f"sign_be_comm_async_{key.decode('utf-8')}")
            signal.emit(msg)


class AsyncReceiver(object):
    def __init__(self, backend):
        self._be = backend
        self._async_signals = AsyncSignalerCB(backend=backend)
        self._async_stats_cb = AsyncStatsCB()
        self._register_asyncs()

    def keys(self):
        return self._async_stats_cb.keys()

    def last(self, key):
        return self._async_stats_cb.last(key)

    def stats(self):
        return self._async_stats_cb.stats()

    @property
    def proc(self):
        return self._async_stats_cb

    def _register_all(self, async_callback):
        if not isinstance(async_callback, AsyncCallback):
            log.warning(f"Tried to register callback of type: {type(async_callback)}. \n Not registering anything")
            return
        self._be.comm_client.async_subscribe('app_cmd', async_callback)
        # This should be in a module handler but I do not have time now
        # For each module that generates asyncs, register it here, so you have the signaler functionality for that async
        self._be.comm_client.async_subscribe('modex_random_number', async_callback)
        self._be.comm_client.async_subscribe('modpiratstemp_current_temp', async_callback)
        self._be.comm_client.async_subscribe('modpiratsweight_current_weight', async_callback)
        self._be.comm_client.async_subscribe('modpiratsvoltage_current_voltage', async_callback)
        self._be.comm_client.async_subscribe('modpiratspressure_current_pressure', async_callback)

    def _register_asyncs(self):
        # This ones simply keep count of how many asyncs have been received of each type and holds the last one
        self._register_all(self._async_stats_cb)
        # This ones will emit signals
        self._register_all(self._async_signals)
