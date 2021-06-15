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

from simplecs.server.modules.modbase import ModuleBase
from simplecs.server.commands import Command, CommandSet

log = get_logger('Pirats_Temp_Mod_For_Cli')


class ModPiratsTempCommand(Command):
    # Just a base class that defines where the module is inside of the app, so it does not have to be defined on every command
    # In this example does not make much sense because there is only one command

    @property
    def module(self):
        return self.app.mod_handler.get_mod('modpiratstemp')


class EchoTempCommand(ModPiratsTempCommand):
    # Command has two attributes: app and _kwargs
    # kwargs allows to get a dictionary with parameters for the command to be executed

    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)


class SetTempChannel(ModPiratsTempCommand):

    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set measurement temp channel to: '{val}'")
        return self.module.set_temp_channel(temp_channel=val)


class ModPiratsTempCommandSet(CommandSet):
    # Class that lists the commands implemented by a module
    # It is only a dictionary with the commands available
    # The key specifies the command name for which the client should call it
    # the value of the dict must be a Command inherited class
    _commands_available = {
        'echo': EchoTempCommand,
        'set_temp_channel': SetTempChannel
    }


class ModPiratsTempBase(ModuleBase):

    # Next class attributes are mandatory
    # _command_set is used by the module_handler to execute commands as well as the client that gets the list of
    #   available commands from it
    # _mod_name
    # _async_topics is used as documentation and at the client to list the available asyncs comming from this module

    # Once the executer have found a module that it's name matches the first part of the command, it will check if
    # the module has the 'command_name' command implemented.
    # mod_commands must be a CommandSet inherited class (class, not instance, although it would probably work also)
    _command_set = ModPiratsTempCommandSet  # The class not the instance
    # mod_name is what sets the prefix for the received commands. Each module must have a different mod_name
    # When the executer receives a command, it must have a command name like: 'module_name.command_name'
    # The executer will check which module should contain that command using the modules mod_name property
    _mod_name = 'modpiratstemp'
    # Best practice for async_topics is to use the name of the module + _ + name of async to avoid having duplicates
    # with other modules
    _async_topics = ['modpiratstemp_current_temp']