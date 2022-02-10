#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a Module for reading the Pressure Sense for the client side

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '26/1/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
from piratscs.server.modules.modPressureSenseServerBase import ModPressureSenseBase as ServerModPressureSense
from piratscs.client.modules.modbase import ClientModuleBase

log = get_logger('client_pressure_sense_mod')


class ModPressureSense(ClientModuleBase):
    _mod_name = ServerModPressureSense.get_mod_name()
    _commands = ServerModPressureSense.get_command_list()
    _async_topics = ServerModPressureSense.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def start_acq(self):
        command = self.mod_name + '.' + 'start_acq'
        return self._client.command(command=command)

    def stop_acq(self):
        command = self.mod_name + '.' + 'stop_acq'
        return self._client.command(command=command)

    def set_pressure_channel(self, pressure_channel):
        command = self.mod_name + '.' + 'set_pressure_channel'
        kwargs = {'value': pressure_channel}
        return self._client.command(command=command, kwargs=kwargs)

    def set_period(self, period):
        command = self.mod_name + '.' + 'set_period'
        kwargs = {'value': period}
        return self._client.command(command=command, kwargs=kwargs)
