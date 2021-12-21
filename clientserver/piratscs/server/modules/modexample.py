#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module

The module has  commands implemented as well as a thread that publishes data

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '19/2/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from piratscs.logger import get_logger
from random import random
import datetime
from threading import Thread, Event

from piratscs.server.modules.modbase import ModuleBase
from piratscs.server.commands import Command, CommandSet

import numbers
log = get_logger('example_mod')


class ModExampleCommand(Command):
    # Just a base class that defines where the module is inside of the app, so it does not have to be defined on every command
    # In this example does not make much sense because there is only one command

    @property
    def module(self):
        return self.app.mod_handler.get_mod('modex')


class EchoCommand(ModExampleCommand):
    # Command has two attributes: app and _kwargs
    # kwargs allows to get a dictionary with parameters for the command to be executed

    def execute(self):
        val = self._kwargs.get('value', None)
        if val is None:
            log.debug('Asked to echo a \'None\' value')
        return self.module.echo(whatever=val)


class SetMaxRandom(ModExampleCommand):

    def execute(self):
        val = self._kwargs.get('value', None)
        log.debug(f"Asked to set max random to: '{val}'")
        return self.module.set_max_rnd(max_rnd=val)


class ModExampleCommandSet(CommandSet):
    # Class that lists the commands implemented by a module
    # It is only a dictionary with the commands available
    # The key specifies the command name for which the client should call it
    # the value of the dict must be a Command inherited class
    _commands_available = {
        'echo': EchoCommand,
        'set_max_rnd': SetMaxRandom
    }


class ModExample(ModuleBase):

    # Next class attributes are mandatory
    # _command_set is used by the module_handler to execute commands as well as the client that gets the list of
    #   available commands from it
    # _mod_name
    # _async_topics is used as documentation and at the client to list the available asyncs comming from this module

    # Once the executer have found a module that it's name matches the first part of the command, it will check if
    # the module has the 'command_name' command implemented.
    # mod_commands must be a CommandSet inherited class (class, not instance, although it would probably work also)
    _command_set = ModExampleCommandSet  # The class not the instance
    # mod_name is what sets the prefix for the received commands. Each module must have a different mod_name
    # When the executer receives a command, it must have a command name like: 'module_name.command_name'
    # The executer will check which module should contain that command using the modules mod_name property
    _mod_name = 'modex'
    # Best practice for async_topics is to use the name of the module + _ + name of async to avoid having duplicates
    # with other modules
    _async_topics = ['modex_random_number']

    def __init__(self, app):
        super().__init__(app=app)
        self._th = Thread(target=self._run)
        self._th_out = Event()
        self._max_rnd = 100

    def _pub_rnd(self, value):
        # This is what actually publishes the number to the clients
        # Make sure that the topic used here is the same on cls._async_topics
        # It is a good policy to use the name of the module as a prefix
        # Do not separate the topics with dots or dashes, name of the topic must be a valid python variable name
        self.app.server.pub_async('modex_random_number', value)

    def _run(self):
        # What is executed inside the thread
        count = 0
        while not self._th_out.wait(0.1):
            t = {'ts': datetime.datetime.utcnow().timestamp(),
                 'random': self._max_rnd * random()}
            self._pub_rnd(t)
            count += 1
            if count % 100 == 0:
                log.debug(f'Published {count} randoms')

    def initialize(self):
        # This method is called when the module is loaded
        # It is not mandatory to implement it, but it is a good practice to do so
        # It is called after the constructor
        self.start()

    def start(self):
        log.debug('Starting thread on Module Example')
        self._th.start()
        log.debug('Started thread on Module Example')

    def stop(self):
        self._th_out.set()
        # set timeout longer than max wait_time
        self._th.join(timeout=1.1)
        if self._th.is_alive():
            log.error('Module Example thread has not stopped')

    @staticmethod
    def echo(whatever):
        # silly function that returns what has received to show how to implement a command
        return whatever

    def set_max_rnd(self, max_rnd):
        # Another example of a command. It sets the maximum random generated. It shows how to affect the thread
        if isinstance(max_rnd, numbers.Number):
            self._max_rnd = max_rnd
            return True
        try:
            val = float(max_rnd)
            self._max_rnd = val
            return True
        except:
            raise Exception(f'Invalid value for max_rnd ({max_rnd}), it must be a number')
