#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '19/2/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from abc import ABC, abstractmethod


class ModuleBase(ABC):
    _command_set = None
    _async_topics = None
    _mod_name = None

    def __init__(self, app):
        self._app = app

    @property
    def app(self):
        return self._app


    @classmethod
    def get_command_list(cls):
        return cls._command_set.get_command_list()

    @classmethod
    def get_async_topics(cls):
        return cls._async_topics

    @classmethod
    def get_mod_name(cls):
        return cls._mod_name

    @property
    def mod_name(self):
        # mod_name is what sets the prefix for the received commands. Each module must have a different mod_name
        # When the executer receives a command, it must have a command name like: 'module_name.command_name'
        # The executer will check which module should contain that command using the modules mod_name property
        return self._mod_name

    @property
    def mod_commands(self):
        # Once the executer have found a module that it's name matches the first part of the command, it will check if
        # the module has the 'command_name' command implemented.
        # mod_commands must be a CommandSet inherited class (class, not instance, although it would probably work also)
        return self._command_set

    @abstractmethod

    def initialize(self):
        # do any initialization required
        pass

    def start(self):
        # start threads here
        pass

    @abstractmethod
    def stop(self):
        # Stop anything required and all threads
        pass

