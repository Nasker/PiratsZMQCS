#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module

The module has  commands implemented as well as a thread that publishes data

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '08/2/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
import datetime
import time
from threading import Thread, Event
from piratscs.server.modules.modMeasurementsServerBase import ModMeasurementsBase
from piratslib.controlNsensing.VoltageSense import VoltageSense
from piratslib.controlNsensing.WeightSense import WeightSense
from piratslib.controlNsensing.TemperatureSense import TemperatureSense
from pyvsr53dl.vsr53dl import PyVSR53DL

log = get_logger('Pirats_Voltage_Mod')


class ModMeasurements(ModMeasurementsBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pirats_voltage_sense = None
        self._pirats_weight_sense = None
        self._pirats_temperature_sense = None
        self._pressure_sense = None
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._voltage_channels_list = []

    def _pub_current_voltage(self, value):
        self.app.server.pub_async('modpiratsvoltage_current_voltage', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            if self._voltage_channels_list:
                voltages_list = self._pirats_voltage_sense.get_voltages_list(self._voltage_channels_list)
                log.debug(f'VOLTS LIST IN SERVER MODULE {voltages_list}')
                t = {'ts': datetime.datetime.utcnow().timestamp(),
                     'current_voltage': voltages_list}
                self._pub_current_voltage(t)
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} voltages')
            time.sleep(0.5)

    def initialize(self, args=None):
        log.debug('Initializing Module Pirats Voltage')
        self.init_voltage_sense(args[0])
        self.init_weight_sense(args[1])
        self.init_temperature_sense(args[2])
        self.init_pressure_sense(args[3])

    def init_temperature_sense(self, ref=None):
        if ref is None:
            self._pirats_temperature_sense = TemperatureSense()
        else:
            self._pirats_temperature_sense = ref

    def init_voltage_sense(self, ref=None):
        if ref is None:
            self._pirats_voltage_sense = VoltageSense()
        else:
            self._pirats_voltage_sense = ref

    def init_weight_sense(self, ref=None):
        if ref is None:
            NOMINAL_LOAD = 10000
            NOMINAL_OUTPUT = 0.002
            FULL_SCALE_VOLT = 5.0
            self._pirats_weight_sense = WeightSense(NOMINAL_LOAD, NOMINAL_OUTPUT, FULL_SCALE_VOLT)
        else:
            self._pirats_weight_sense = ref

    def init_pressure_sense(self, ref=None):
        if ref is None:
            from pyvsr53dl.sys import dev_tty
            sensor_address = 1
            self._pressure_sense = PyVSR53DL(dev_tty, sensor_address)
            self._pressure_sense.open_communication()
            self._pressure_sense.get_device_type()
        else:
            self._pressure_sense = ref

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
                self._voltage_channels_list = []
            elif not ',' in voltage_channels_str:
                self._voltage_channels_list = [int(voltage_channels_str)]
            else:
                self._voltage_channels_list = list(map(int, voltage_channels_str.split(',')))
            log.debug(self._voltage_channels_list)
            return True
        except:
            raise Exception(f'Invalid value for set channel ({voltage_channels_str}), it must be a number or a list')
