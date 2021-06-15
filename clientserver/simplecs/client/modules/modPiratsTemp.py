#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a Module for reading the Pirats Temperature for the client side

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
from simplecs.server.modules.modPiratsTempBase import ModPiratsTempBase as ServerModPiratsTemplate
from simplecs.client.modules.modbase import ClientModuleBase

log = get_logger('client_pirats_temp_mod')


class ModPiratsTemp(ClientModuleBase):
    _mod_name = ServerModPiratsTemplate.get_mod_name()
    _commands = ServerModPiratsTemplate.get_command_list()
    _async_topics = ServerModPiratsTemplate.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def set_temp_channel(self, temp_channel):
        command = self.mod_name + '.' + 'set_temp_channel'
        kwargs = {'value': temp_channel}
        return self._client.command(command=command, kwargs=kwargs)
