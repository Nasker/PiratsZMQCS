#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module

The module has  commands implemented as well as a thread that publishes data

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2021'
__date__ = '14/6/21'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
import datetime
import time
from threading import Thread, Event
from piratscs.server.modules.modPiratsWeightServerBase import ModPiratsWeightBase

log = get_logger('Pirats_Weight_Mod')


class ModPiratsWeight(ModPiratsWeightBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._weight_channels_list = []
        self._devices = None

    def _pub_current_weight(self, value):
        self.app.server.pub_async('modpiratsweight_current_weight', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            if self._weight_channels_list:
                weights_list = self._devices.get_weight_readings(self._weight_channels_list)
                log.debug(f'WEIGHTS LIST IN SERVER MODULE {weights_list}')
                t = {'ts': datetime.datetime.utcnow().timestamp(),
                     'current_weight': weights_list}
                self._pub_current_weight(t)
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} weights')
            time.sleep(0.5)

    def initialize(self):
        log.debug('Initializing Module Pirats Weight')

    def connect_devices(self, devices_reference):
        self._devices = devices_reference

    def start(self):
        log.debug('Starting thread on Module Pirats Weight')
        if self._th.is_alive():
            log.debug("Thread is already alive")
        else:
            self._th.start()
            log.debug('Started thread on Module Pirats Weight')

    def start_acq(self):
        log.debug('Starting ACQ on Module Pirats Weight')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started ACQ on Module Pirats Weight')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats Weight thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Module Pirats Weight ACQ has stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que pesao!'
        return whatever

    def set_weight_channel(self, weight_channels_str):
        log.info(f'Setting weight channels {weight_channels_str}')
        try:
            if not weight_channels_str:
                self._weight_channels_list = []
            elif not ',' in weight_channels_str:
                self._weight_channels_list = [int(weight_channels_str)]
            else:
                self._weight_channels_list = list(map(int, weight_channels_str.split(',')))
            log.debug(f'WEIGHT CHANNELS LIST: {self._weight_channels_list}')
            return True
        except:
            raise Exception(f'Invalid value for set channel ({weight_channels_str}), it must be a number or a list')
