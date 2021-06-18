#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is an example of a Module for the client side

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
from piratscs.server.modules.modexample import ModExample as ServerModExample
from piratscs.client.modules.modbase import ClientModuleBase

log = get_logger('client_example_mod')


class ModExample(ClientModuleBase):
    _mod_name = ServerModExample.get_mod_name()
    _commands = ServerModExample.get_command_list()
    _async_topics = ServerModExample.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def echo(self, value):
        # check ModExampleCommandSet keys to know what must be put here
        command = self.mod_name + '.' + 'echo'
        kwargs = {'value': value}
        return self._client.command(command=command, kwargs=kwargs)

    def set_max_rnd(self, max_rnd):
        command = self.mod_name + '.' + 'set_max_rnd'
        kwargs = {'value': max_rnd}
        return self._client.command(command=command, kwargs=kwargs)
