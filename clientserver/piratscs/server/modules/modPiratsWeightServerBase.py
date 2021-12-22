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

log = get_logger('Pirats_Weight_Mod_For_Cli')

class ModPiratsWeightCommand(Command):
    @property
    def module(self):
        return self.app.mod_handler.get_mod('modpiratsweight')


class EchoWeightCommand(ModPiratsWeightCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)

class StartAcqCommand(ModPiratsWeightCommand):
    def execute(self):
        log.debug("Asked to start weight acquisition")
        return self.module.start_acq()

class StopAcqCommand(ModPiratsWeightCommand):
    def execute(self):
        log.debug("Asked to start weight acquisition")
        return self.module.stop_acq()

class SetWeightChannel(ModPiratsWeightCommand):
    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement weight channel to: '{val}'")
        return self.module.set_weight_channel(val)

class ModPiratsWeightCommandSet(CommandSet):
    _commands_available = {
        'echo': EchoWeightCommand,
        'start_acq': StartAcqCommand,
        'stop_acq': StopAcqCommand,
        'set_weight_channel': SetWeightChannel
    }

class ModPiratsWeightBase(ModuleBase):
    _command_set = ModPiratsWeightCommandSet  # The class not the instance
    _mod_name = 'modpiratsweight'
    _async_topics = ['modpiratsweight_current_weight']
