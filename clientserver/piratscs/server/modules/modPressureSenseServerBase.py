#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module modPressureSenseServerBase.py:
The module has  commands implemented as well as a thread that publishes data
"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '26/1/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
from piratscs.server.modules.modbase import ModuleBase
from piratscs.server.commands import Command, CommandSet

log = get_logger('Pressure_Sense_Mod_For_Cli')


class ModPressureSenseCommand(Command):
    @property
    def module(self):
        return self.app.mod_handler.get_mod('modpressuresense')


class EchoPressureCommand(ModPressureSenseCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)


class StartAcqCommand(ModPressureSenseCommand):
    def execute(self):
        log.debug("Asked to start pressure acquisition")
        return self.module.start_acq()


class StopAcqCommand(ModPressureSenseCommand):
    def execute(self):
        log.debug("Asked to start pressure acquisition")
        return self.module.stop_acq()


class SetPressureChannel(ModPressureSenseCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement pressure channel to: '{val}'")
        return self.module.set_pressure_channel(val)

class SetPeriod(ModPressureSenseCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set pressure period to: '{val}'")
        return self.module.set_period(val)

class ModPressureSenseCommandSet(CommandSet):
    _commands_available = {
        'echo': EchoPressureCommand,
        'start_acq': StartAcqCommand,
        'stop_acq': StopAcqCommand,
        'set_pressure_channel': SetPressureChannel,
        'set_period': SetPeriod
    }


class ModPressureSenseBase(ModuleBase):
    _command_set = ModPressureSenseCommandSet  # The class not the instance
    _mod_name = 'modpressuresense'
    _async_topics = ['modpressuresense_current_pressure']
