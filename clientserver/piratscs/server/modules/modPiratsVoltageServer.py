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
from piratscs.server.modules.modPiratsVoltageServerBase import ModPiratsVoltageBase

log = get_logger('Pirats_Voltage_Mod')


class ModPiratsVoltage(ModPiratsVoltageBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._devices = None
        self._period = 0.5

    def _pub_current_measurements(self, values):
        self.app.server.pub_async('modpiratstemp_current_temp', values[0])
        self.app.server.pub_async('modpressure_current_pressure', values[1])
        self.app.server.pub_async('modpiratsweight_current_weight', values[2])
        self.app.server.pub_async('modpiratsvoltage_current_voltage', values[3])


    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            if self._devices.voltage_channels:
                voltages_list = self._devices.get_voltage_readings()
                log.debug(f'VOLTS LIST IN SERVER MODULE {voltages_list}')
                t = {'ts': datetime.datetime.utcnow().timestamp(),
                     'current_voltage': voltages_list}
                self._pub_current_measurements(t)
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} voltages')
            time.sleep(self._period)

    def initialize(self):
        log.debug('Initializing Module Pirats Voltage')

    def connect_devices(self, devices_reference):
        self._devices = devices_reference

    def start(self):
        log.debug('Starting thread on Module Pirats Voltage')
        self._th.start()
        log.debug('Started thread on Module Pirats Voltage')

    def start_acq(self):
        log.debug('Starting ACQ on Module Pirats Voltage')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started ACQ on Module Pirats Voltage')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats Voltage thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Module Pirats Voltage ACQ has stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que chispa!'
        return whatever

    def set_voltage_channel(self, voltage_channels_str):
        try:
            if not voltage_channels_str:
                voltage_channels_list = []
            elif not ',' in voltage_channels_str:
                voltage_channels_list = [int(voltage_channels_str)]
            else:
                voltage_channels_list = list(map(int, voltage_channels_str.split(',')))
            log.debug(voltage_channels_list)
            self._devices.voltage_channels = voltage_channels_list
            return True
        except:
            raise Exception(f'Invalid value for set channel ({voltage_channels_str}), it must be a number or a list')

    def set_period(self, period):
        try:
            period = float(period)
            if period < 0.01:
                raise Exception('Period must be greater than 0.01')
            self._period = period
            return True
        except:
            raise Exception(f'Invalid value for set period ({period}), it must be a number')

