#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module modPressureSenseServerBase.py:

The module has  commands implemented as well as a thread that publishes data

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '26/1/21'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
import datetime
import time
from threading import Thread, Event
from piratscs.server.modules.modPressureSenseServerBase import ModPressureSenseBase
from pyvsr53dl.vsr53dl import PyVSR53DL

log = get_logger('Pressure_Sense_Mod')


class ModPressureSense(ModPressureSenseBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pressure_sense = None
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._pressure_channels_list = []

    def _pub_current_pressure(self, value):
        self.app.server.pub_async('modpressuresense_current_pressure', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            if self._pressure_channels_list:
                #pressures_list = [self._pressure_sense.get_measurement_value()]
                pressures_list = [23.4]
                log.debug(f'PRESSURES LIST IN SERVER MODULE {pressures_list}')
                t = {'ts': datetime.datetime.utcnow().timestamp(),
                     'current_voltage': pressures_list}
                self._pub_current_pressure(t)
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} pressures')
            time.sleep(1.0)

    def initialize(self):
        log.debug('Initializing Module Pressure Sense')
        from pyvsr53dl.sys import dev_tty
        sensor_address = 1
        # self._pressure_sense = PyVSR53DL(dev_tty, sensor_address)
        # self._pressure_sense.open_communication()
        # self._pressure_sense.get_device_type()

    def start(self):
        log.debug('Starting thread on Module Pressure Sense')
        self._th.start()
        log.debug('Started thread on Module Pressure Sense')

    def start_acq(self):
        log.debug('Starting ACQ on Module Pressure Sense')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started ACQ on Module Pressure Sense')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pressure Sense thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Module Pressure Sense ACQ has stopped')


    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que presión!'
        return whatever

    def set_pressure_channel(self, pressure_channels_str):
        try:
            if not pressure_channels_str:
                self._pressure_channels_list = []
            elif not ',' in pressure_channels_str:
                self._pressure_channels_list = [int(pressure_channels_str)]
            else:
                self._pressure_channels_list = list(map(int, pressure_channels_str.split(',')))
            log.debug(self._pressure_channels_list)
            return True
        except:
            raise Exception(f'Invalid value for set channel ({pressure_channels_str}), it must be a number or a list')
