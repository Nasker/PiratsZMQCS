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
import time
from threading import Thread, Event
from piratscs.server.modules.modMeasurementsServerBase import ModMeasurementsBase
from piratscs.server.measurements_manager.MeasurementsManager import MeasurementsManager

log = get_logger('Measurements_Mod')


class ModMeasurements(ModMeasurementsBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()
        self._devices = None
        self._period = 0.5
        self._current_filename = None
        self._measurement_manager = MeasurementsManager()

    def _pub_current_measurements(self, value):
        """self.app.server.pub_async('modpiratstemp_current_temp', value)
        self.app.server.pub_async('modpressure_current_pressure', value)
        self.app.server.pub_async('modpiratsweight_current_weight', value)
        self.app.server.pub_async('modpiratsvoltage_current_voltage', value)
        """

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            if self._devices.current_devices_list:
                count += 1
                if count % 100 == 0:
                    log.debug(f'Published {count} voltages')
            time.sleep(self._period)

    def initialize(self, args=None):
        log.debug('Initializing Measurement Modules')

    def connect_devices(self, devices_reference):
        self._devices = devices_reference

    def start(self):
        log.debug('Starting thread on Measurement Modules')
        self._th.start()
        log.debug('Started thread on Measurement Modules')

    def start_acq(self):
        log.debug('Starting ACQ on Measurement Modules')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started ACQ on Measurement Modules')
            self._measurement_manager.create_measurements_file(self._current_filename,
                                                               self._devices.get_measurements_header())

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Measurement Modules thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Measurement Modules ACQ has stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} medime esta!'
        return whatever

    def select_measurements(self, measurements_list_str):
        try:
            if not measurements_list_str:
                self._devices.current_devices_list = []
            elif not ',' in measurements_list_str:
                self._devices.current_devices_list  = [int(measurements_list_str)]
            else:
                self._devices.current_devices_list = list(map(int, measurements_list_str.split(',')))
            log.debug(self._devices.current_devices_list )
            return True
        except:
            raise Exception(f'Invalid value for select measurements ({self._devices.current_devices_list }), '
                            f'it must be a number or a list')

    def set_period(self, period):
        try:
            period = float(period)
            if period < 0.01:
                raise Exception('Period must be greater than 0.01')
            self._period = period
            return True
        except:
            raise Exception(f'Invalid value for set period ({period}), it must be a number')

    def set_file_name(self, filename):
        try:
            self._current_filename = filename
            return True
        except:
            raise Exception(f'Invalid value for set filename ({filename}), it must be a string')