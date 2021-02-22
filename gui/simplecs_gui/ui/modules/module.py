#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '27/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

from abc import ABC


class Module(ABC):

    def __init__(self, parent=None):
        self._parent = parent
        self._miniwidget = None
        self._action = None

    @property
    def action(self):
        return self._action

    def set_action_to_toolbar(self):
        if self.action:
            self._parent.toolbar.addAction(self.action)

    def add_miniwidget(self):
        if self._miniwidget:
            self._parent.minisbar.addWidget(self._miniwidget)

    def close(self):
        pass