#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A simple python script

"""
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '26/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'

import os
import logging
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QColor, QIcon, QFont, QFontDatabase


from piratscs_gui.ui.modules.logger_window.logger_window_ui import Ui_LoggerWindow
from piratscs_gui.system.logger import formatter

from piratscs_gui.ui.modules.module import Module
from piratscs_gui.system.logger import get_logger
log = get_logger('logwindow')


class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self._textedit = parent

    def emit(self, record):
        msg = self.format(record)
        if record.levelno == logging.DEBUG:
            self._textedit.setTextColor(QColor(245, 215, 66))
        elif record.levelno == logging.INFO:
            self._textedit.setTextColor(QColor(71, 196, 75))
        elif record.levelno == logging.WARNING:
            self._textedit.setTextColor(QColor(219, 153, 9))
        elif record.levelno > logging.WARNING:
            self._textedit.setTextColor(QColor(186, 28, 44))
        self._textedit.append(msg)


class LoggerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self.qtexteditlogger = QTextEditLogger(self._ui.textEdit)
        self.qtexteditlogger.setFormatter(formatter)
        logging.getLogger().addHandler(self.qtexteditlogger)

    def _setup_ui(self):
        try:
            CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
            font_path = os.path.join(CURRENT_DIRECTORY, "fonts", "RobotoMono-Regular.ttf")
            _id = QFontDatabase.addApplicationFont(font_path)
            if QFontDatabase.applicationFontFamilies(_id) == -1:
                log.error(f"problem loading font 'RobotoMono-Regular.ttf'")
        except:
            log.exception('Failed to load Roboto Mono font')

        self._ui = Ui_LoggerWindow()
        self._ui.setupUi(self)
        robotomono = QFont("Roboto")
        self._ui.textEdit.setFont(robotomono)
        self._ui.textEdit.setFontPointSize(15)


class LoggerWindowModule(Module):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # parent = None because it goes in a separate window
        self._widget = LoggerWindow(parent=None)
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'iconlogviewer.png')
        action = QAction(QIcon(ico_path), "View logs", self._parent)
        action.setStatusTip("Open a log viewer")
        action.triggered.connect(self.action_function)
        return action

    def action_function(self):
        self._widget.show()

    def close(self):
        self._widget.close()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = LoggerWindow()
    window.show()
    app.exec_()
