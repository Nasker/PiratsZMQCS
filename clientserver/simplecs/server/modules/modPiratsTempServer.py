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

from simplecs.logger import get_logger
import datetime
from threading import Thread, Event
from simplecs.server.modules.modPiratsTempServerBase import ModPiratsTempBase
from piratslib.controlNsensing.TemperatureSense import TemperatureSense

import numbers
log = get_logger('Pirats_Temp_Mod')


class ModPiratsTemp(ModPiratsTempBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pirats_temp_sense = None
        self._th_out = Event()
        self._temp_channels_list = [1]

    def _pub_current_temp(self, value):
        self.app.server.pub_async('modpiratstemp_current_temp', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while not self._th_out.wait(0.1 ):
            temps_list = self._pirats_temp_sense.get_temps_list(self._temp_channels_list)
            # log.debug(f'TEMPS LIST IN SERVER MODULE {temps_list}')
            t = {'ts': datetime.datetime.utcnow().timestamp(),
                 'current_temp': temps_list}
            self._pub_current_temp(t)
            count += 1
            if count % 100 == 0:
                log.debug(f'Published {count} temperatures')

    def start(self):
        log.debug('Starting thread on Module Pirats Temp')
        self._pirats_temp_sense = TemperatureSense()
        self._th.start()
        log.debug('Started thread on Module Pirats Temp')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats Temp thread has not stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        whatever = f'{whatever} que caló!'
        return whatever

    def set_temp_channel(self, temp_channels_str):
        try:
            if not ',' in temp_channels_str:
                self._temp_channels_list = [int(temp_channels_str)]
            else:
                self._temp_channels_list = list(map(int, temp_channels_str.split(',')))
            log.debug(self._temp_channels_list)
            return True
        except:
            raise Exception(f'Invalid value for set channel ({temp_channels_str}), it must be a number or a list')
