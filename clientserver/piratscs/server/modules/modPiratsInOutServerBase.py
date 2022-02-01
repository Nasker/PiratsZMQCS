#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module
The module has  commands implemented as well as a thread that publishes data
"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '31/01/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
from piratscs.server.modules.modbase import ModuleBase
from piratscs.server.commands import Command, CommandSet

log = get_logger('Pirats_InOut_Mod_For_Cli')

class ModPiratsInOutCommand(Command):
    @property
    def module(self):
        return self.app.mod_handler.get_mod('modpiratsinout')


class EchoInOutCommand(ModPiratsInOutCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)

class StartAcqCommand(ModPiratsInOutCommand):
    def execute(self):
        log.debug("Asked to start inout acquisition")
        return self.module.start_acq()

class StopAcqCommand(ModPiratsInOutCommand):
    def execute(self):
        log.debug("Asked to start inout acquisition")
        return self.module.stop_acq()

class SetInOutChannel(ModPiratsInOutCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement voltage channel to: '{val}'")
        return self.module.set_voltage_channel(val)

class ModPiratsVoltageCommandSet(CommandSet):
    _commands_available = {
        'echo': EchoInOutCommand,
        'start_acq': StartAcqCommand,
        'stop_acq': StopAcqCommand,
        'set_voltage_channel': SetInOutChannel
    }

class ModPiratsVoltageBase(ModuleBase):
    _command_set = ModPiratsVoltageCommandSet  # The class not the instance
    _mod_name = 'modpiratsvoltage'
    _async_topics = ['modpiratsvoltage_current_voltage']
