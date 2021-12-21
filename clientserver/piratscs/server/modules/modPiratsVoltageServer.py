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
from threading import Thread, Event
from piratscs.server.modules.modPiratsVoltageServerBase import ModPiratsVoltageBase
from piratslib.controlNsensing.VoltageSense import VoltageSense

log = get_logger('Pirats_Voltage_Mod')


class ModPiratsVoltage(ModPiratsVoltageBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pirats_voltage_sense = None
        self._th_out = Event()
        self._voltage_channels_list = [0]

    def _pub_current_voltage(self, value):
        self.app.server.pub_async('modpiratsvoltage_current_voltage', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while not self._th_out.wait(0.1):
            voltages_list = self._pirats_voltage_sense.get_voltages_list(self._voltage_channels_list)
            # log.debug(f'TEMPS LIST IN SERVER MODULE {voltages_list}')
            t = {'ts': datetime.datetime.utcnow().timestamp(),
                 'current_voltage': voltages_list}
            self._pub_current_voltage(t)
            count += 1
            if count % 100 == 0:
                log.debug(f'Published {count} voltages')

    def initialize(self):
        log.debug('Initializing Module Pirats Voltage')
        self._pirats_voltage_sense = VoltageSense()

    def start(self):
        log.debug('Starting thread on Module Pirats Voltage')
        self._th.start()
        log.debug('Started thread on Module Pirats Voltage')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats Voltage thread has not stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que chispa!'
        return whatever

    def set_voltage_channel(self, voltage_channels_str):
        try:
            if not ',' in voltage_channels_str:
                self._voltage_channels_list = [int(voltage_channels_str)]
            else:
                self._voltage_channels_list = list(map(int, voltage_channels_str.split(',')))
            log.debug(self._voltage_channels_list)
            return True
        except:
            raise Exception(f'Invalid value for set channel ({voltage_channels_str}), it must be a number or a list')
