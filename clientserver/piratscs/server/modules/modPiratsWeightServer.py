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
from piratslib.controlNsensing.WeightSense import WeightSense

log = get_logger('Pirats_Weight_Mod')


class ModPiratsWeight(ModPiratsWeightBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pirats_weight_sense = None
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._weight_channels_list = []

    def _pub_current_weight(self, value):
        self.app.server.pub_async('modpiratsweight_current_weight', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            weights_list = self._pirats_weight_sense.get_weights_list(self._weight_channels_list)
            if weights_list:
                t = {'ts': datetime.datetime.utcnow().timestamp(),
                     'current_weight': weights_list}
                self._pub_current_weight(t)
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} weights')
                time.sleep(0.5)

    def initialize(self):
        NOMINAL_LOAD = 10000
        NOMINAL_OUTPUT = 0.002
        FULL_SCALE_VOLT = 5.0
        log.debug('Initializing module Pirats Weight')
        self._pirats_weight_sense = WeightSense(NOMINAL_LOAD, NOMINAL_OUTPUT, FULL_SCALE_VOLT)

    def start(self):
        log.debug('Starting thread on Module Pirats Weight')
        if self._th.is_alive():
            log.debug("Thread is already alive")
        else:
            self._th.start()
            log.debug('Started thread on Module Pirats Weight')

    def start_acq(self):
        log.debug('Starting thread on Module Pirats Weight')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started thread on Module Pirats Weight')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats Weight thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Module Pirats Weight thread has stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que pesao!'
        return whatever

    def set_weight_channel(self, weight_channels_str):
        try:
            if not weight_channels_str:
                self._weight_channels_list = []
            elif not ',' in weight_channels_str:
                self._weight_channels_list = [int(weight_channels_str)]
            else:
                self._weight_channels_list = list(map(int, weight_channels_str.split(',')))
            log.debug(self._weight_channels_list)
            return True
        except:
            raise Exception(f'Invalid value for set channel ({weight_channels_str}), it must be a number or a list')
