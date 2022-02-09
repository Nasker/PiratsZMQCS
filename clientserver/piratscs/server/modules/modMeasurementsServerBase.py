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
from piratscs.server.modules.modbase import ModuleBase
from piratscs.server.commands import Command, CommandSet

log = get_logger('Measurements_Mod_For_Cli')

class ModMeasurementsCommand(Command):
    @property
    def module(self):
        return self.app.mod_handler.get_mod('modmeasurements')


class EchoMeasurementsCommand(ModMeasurementsCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)

class StartAcqCommand(ModMeasurementsCommand):
    def execute(self):
        log.debug("Asked to start measurements acquisition")
        return self.module.start_acq()

class StopAcqCommand(ModMeasurementsCommand):
    def execute(self):
        log.debug("Asked to start measurements acquisition")
        return self.module.stop_acq()

class SetMeasurements(ModMeasurementsCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement selection to: '{val}'")
        return self.module.set_measurements(val)

class SetPeriod(ModMeasurementsCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurements period to: '{val}'")
        return self.module.set_period(val)

class ModMeasurementsCommandSet(CommandSet):
    _commands_available = {
        'echo': EchoMeasurementsCommand,
        'start_acq': StartAcqCommand,
        'stop_acq': StopAcqCommand,
        'set_measurements': SetMeasurements,
        'set_period': SetPeriod
    }

class ModMeasurementsBase(ModuleBase):
    _command_set = ModMeasurementsCommandSet  # The class not the instance
    _mod_name = 'momeasurements'
    _async_topics = ['modmeasurements_current_measurements']
