#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A module base to expand functionality on client based on modules loaded in the server

For each module developed for the server, a new module should be created at the client to access its functionality
for the commands point of view.

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '22/2/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'


class ClientModuleBase:

    _mod_name = None
    _async_topics = None
    _commands = None

    def __init__(self, client):
        self._client = client

    @property
    def mod_name(self):
        return self._mod_name

    @property
    def topics(self):
        return self._async_topics

    @property
    def commands(self):
        return self._commands

    def list_commands(self):
        cmds = self.commands.copy()
        cmds += ['list_commands', 'list_topics']
        return cmds

    def list_topics(self):
        return self.topics
