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

from piratscs.server.modules.modbase import ModuleBase
from piratscs.server.commands import Command, CommandSet

log = get_logger('Pirats_Temp_Mod_For_Cli')

class ModPiratsTempCommand(Command):
    @property
    def module(self):
        return self.app.mod_handler.get_mod('modpiratstemp')


class EchoTempCommand(ModPiratsTempCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)

class StartAcqCommand(ModPiratsTempCommand):
    def execute(self):
        log.debug("Asked to start temperature acquisition")
        return self.module.start_acq()

class StopAcqCommand(ModPiratsTempCommand):
    def execute(self):
        log.debug("Asked to start temperature acquisition")
        return self.module.stop_acq()

class SetTempChannel(ModPiratsTempCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement temp channel to: '{val}'")
        return self.module.set_temp_channel(val)

class ModPiratsTempCommandSet(CommandSet):
    _commands_available = {
        'echo': EchoTempCommand,
        'start_acq': StartAcqCommand,
        'stop_acq': StopAcqCommand,
        'set_temp_channel': SetTempChannel
    }

class ModPiratsTempBase(ModuleBase):
    _command_set = ModPiratsTempCommandSet  # The class not the instance
    _mod_name = 'modpiratstemp'
    _async_topics = ['modpiratstemp_current_temp']
