#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module

The module has  commands implemented as well as a thread that publishes data

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '02/2/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
import datetime
import time
from threading import Thread, Event
from piratscs.server.modules.modPiratsInOutServerBase import ModPiratsInOutBase
from piratslib.controlNsensing.DigitalOutputControl import DigitalOutputControl
from piratslib.controlNsensing.DigitalInputSense import DigitalInputSense

log = get_logger('Pirats_Voltage_Mod')


class ModPiratsInOut(ModPiratsInOutBase):

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._pirats_in_sense = None
        self._pirats_out_control = None
        self._th_out = Event()
        self._th_out.set()
        self._flag = Event()

    def _pub_current_state(self, value):
        self.app.server.pub_async('modpiratsinout_current_input_state', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while self._th_out.is_set():
            self._flag.wait()
            inputs_states_list = self._pirats_in_sense.digital_read_all()
            t = {'ts': datetime.datetime.utcnow().timestamp(),
                 'current_inputs_state': inputs_states_list}
            self._pub_current_state(t)
            count += 1
            if count % 100 == 0:
                log.debug(f'Published {count} input readings')
            time.sleep(1.0)

    def initialize(self):
        log.debug('Initializing Module Pirats InOut')
        self._pirats_in_sense = DigitalInputSense()
        self._pirats_out_control = DigitalOutputControl()

    def start(self):
        log.debug('Starting thread on Module Pirats InOut')
        self._th.start()
        log.debug('Started thread on Module Pirats InOut')

    def start_acq(self):
        log.debug('Starting ACQ on Module Pirats InOut')
        if self._th.is_alive():
            self._flag.set()
            log.debug("Thread is already alive")
        else:
            self._th.start()
            self._flag.set()
            log.debug('Started ACQ on Module Pirats InOut')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Pirats InOut thread has not stopped')

    def stop_acq(self):
        self._th_out.set()
        self._flag.clear()
        log.info('Module Pirats InOut ACQ has stopped')

    @staticmethod
    def echo(whatever):
        whatever = f'{whatever} que chispa!'
        return whatever

    def set_output_state(self, output, state):
        log.debug(f'Setting output {output} to state {state}')
        try:
            self._pirats_out_control.digital_write(output, state)
            return True
        except:
            raise Exception(f'Invalid value for output #{output} with state: {state}')
