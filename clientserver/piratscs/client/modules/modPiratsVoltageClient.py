#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a Module for reading the Pirats Voltageerature for the client side

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
from piratscs.server.modules.modPiratsVoltageServerBase import ModPiratsVoltageBase as ServerModPiratsVoltage
from piratscs.client.modules.modbase import ClientModuleBase

log = get_logger('client_pirats_voltage_mod')


class ModPiratsVoltage(ClientModuleBase):
    _mod_name = ServerModPiratsVoltage.get_mod_name()
    _commands = ServerModPiratsVoltage.get_command_list()
    _async_topics = ServerModPiratsVoltage.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def set_voltage_channel(self, voltage_channel):
        command = self.mod_name + '.' + 'set_voltage_channel'
        kwargs = {'value': voltage_channel}
        return self._client.command(command=command, kwargs=kwargs)
