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


class Command(ABC):
    def __init__(self, app, ** kwargs):
        self._app = app
        self._kwargs = kwargs

    @abstractmethod
    def execute(self):
        pass

    @property
    def app(self):
        return self._app

    @property
    @abstractmethod
    def module(self):
        pass


class CommandSet:
    _commands_available = {}

    @classmethod
    def find_command_by_name(cls, command_name):
        return cls._commands_available.get(command_name, None)

    @classmethod
    def get_command_list(cls):
        return list(cls._commands_available.keys())
