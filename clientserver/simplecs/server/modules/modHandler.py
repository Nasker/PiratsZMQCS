#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '19/2/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import traceback
from simplecs.server.modules.modbase import ModuleBase
from simplecs.server.commands import Command
from simplecs.logger import get_logger

log = get_logger('modhandler')


class ModHandler:

    def __init__(self, app):
        self._app = app
        self._modules = {}

    @property
    def app(self):
        return self._app

    def get_mod(self, mod_name):
        return self._modules.get(mod_name, None)

    def register_module(self, mod):
        if not isinstance(mod, ModuleBase):
            raise Exception('module must be an instance of type ModuleBase')
        self._modules[mod.mod_name] = mod

    @staticmethod
    def _execute_command(command):
        assert isinstance(command, Command)
        result = command.execute()
        return result

    def execute_command(self, cmd_msg):
        """
        :param cmd_msg: is an instance of CommandMSG. It contains both the command name as well as the arguments
        :return: Must return a json serializable value. The output of the requested command or an exception
        """
        # This function is executed inside a try catch on the ZMQServer. If an exception is catched, the error
        # field of the answer will be filled
        cmd_fields = cmd_msg.command.split('.')
        mod_name = cmd_fields[0]
        command_name = '.'.join(cmd_fields[1:])
        mod = self._modules.get(mod_name, None)
        if mod is None:
            raise Exception(f'Module named {mod_name} not found!')
        command_class = mod.mod_commands.find_command_by_name(command_name)
        if command_class is None:
            raise Exception(f'Module named {mod_name} does not have a command named {command_name}')
        try:
            ret = self._execute_command(command_class(app=self.app, **cmd_msg.kwargs))
        except Exception:
            log.exception(f"Exception while executing command: {cmd_msg.command} with arguments {str(cmd_msg.kwargs)}")
            self._pub_cmd_ret({'cmd': cmd_msg.command, 'kwargs': cmd_msg.kwargs, 'error': traceback.format_exc()})
            raise
        else:
            self._pub_cmd_ret({'cmd': cmd_msg.command, 'kwargs': cmd_msg.kwargs, 'ans': ret})
            return ret

    def _pub_cmd_ret(self, value):
        self.app.server.pub_cmd_ret(value)


    def start(self):
        # Iterate over all loaded modules and execute its start method
        for k, mod in self._modules.items():
            try:
                mod.start()
            except:
                log.exception('Exception rise when starting module')
            else:
                log.info(f"Started module '{mod.__class__.__name__}'")

    def stop(self):
        # Iterate over all loaded modules and execute its stop method
        for k, mod in self._modules.items():
            try:
                mod.stop()
            except:
                log.exception('Exception rise when stopping module')
            else:
                log.info(f"Stopped module '{mod.__class__.__name__}'")
