#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This is a Module for reading the Pirats Voltageerature for the client side

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '11/2/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

from piratscs.logger import get_logger
from piratscs.server.modules.modMeasurementsServerBase import ModMeasurementsBase as ServerModMeasurements
from piratscs.client.modules.modbase import ClientModuleBase

log = get_logger('client_pirats_voltage_mod')


class ModMeasurements(ClientModuleBase):
    _mod_name = ServerModMeasurements.get_mod_name()
    _commands = ServerModMeasurements.get_command_list()
    _async_topics = ServerModMeasurements.get_async_topics()

    def __init__(self, client):
        super().__init__(client=client)

    def start_acq(self):
        command = self.mod_name + '.' + 'start_acq'
        return self._client.command(command=command)

    def stop_acq(self):
        command = self.mod_name + '.' + 'stop_acq'
        return self._client.command(command=command)

    def select_measurements(self, measurements):
        command = self.mod_name + '.' + 'select_measurements'
        kwargs = {'value': measurements}
        return self._client.command(command=command, kwargs=kwargs)

    def set_period(self, period):
        command = self.mod_name + '.' + 'set_period'
        kwargs = {'value': period}
        return self._client.command(command=command, kwargs=kwargs)

    def set_file_name(self, file_name):
        command = self.mod_name + '.' + 'set_file_name'
        kwargs = {'value': file_name}
        return self._client.command(command=command, kwargs=kwargs)

    def get_select_devices_channels(self):
        command = self.mod_name + '.' + 'get_select_devices_channels'
        return self._client.command(command=command)
