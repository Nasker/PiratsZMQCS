#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a Module for reading the Pirats Voltageerature for the client side

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '2/2/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
from piratscs.server.modules.modPiratsInOutServerBase import ModPiratsInOutBase as ServerModPiratsInOut
from piratscs.client.modules.modbase import ClientModuleBase

log = get_logger('client_pirats_voltage_mod')


class ModPiratsInOut(ClientModuleBase):
    _mod_name = ServerModPiratsInOut.get_mod_name()
    _commands = ServerModPiratsInOut.get_command_list()
    _async_topics = ServerModPiratsInOut.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def start_acq(self):
        command = self.mod_name + '.' + 'start_acq'
        return self._client.command(command=command)

    def stop_acq(self):
        command = self.mod_name + '.' + 'stop_acq'
        return self._client.command(command=command)

    def set_output_state(self, output, state):
        command = self.mod_name + '.' + 'set_output_state'
        kwargs = {'output': output, 'state': state}
        return self._client.command(command=command, kwargs=kwargs)
