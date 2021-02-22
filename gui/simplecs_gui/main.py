#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Otger Ballester'
__copyright__ = 'Copyright 2021'
__date__ = '18/1/21'
__credits__ = ['Otger Ballester', ]
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Otger Ballester'
__email__ = 'otger@ifae.es'


if __name__ == '__main__':
    import os
    import sys
    import time

    from PyQt5.QtWidgets import QApplication
    from PyQt5 import QtGui
    from simplecs_gui.system.logger import log
    from simplecs_gui.ui.mainwindow import MainWindow
    from simplecs_gui.system.paths import create_paths_if_not_exists, CONFIG_YAML_FILE_PATH
    create_paths_if_not_exists()
    from simplecs_gui.system.config import SimpleCSQtGUIConf
    conf = SimpleCSQtGUIConf()
    conf.set_file_path(CONFIG_YAML_FILE_PATH)
    if os.path.exists(CONFIG_YAML_FILE_PATH):
        conf.load_yaml(CONFIG_YAML_FILE_PATH)
    conf.save_as_yaml()
    if conf.logging.save_logs:
        from simplecs_gui.system.logger import log_add_file_handler
        log_add_file_handler(conf.logging.log_path)
    if conf.logging.show_stream:
        from simplecs_gui.system.logger import log_add_stream_handler
        log_add_stream_handler()

    from simplecs_gui.backend.backend import Backend
    log.info('Creating backend')
    s = time.time()
    backend = Backend(config=conf)
    log.info(f'Backend created. Took {time.time() - s:.2}s to create the backend')
    app = QApplication(sys.argv)
    window = MainWindow(config=conf, backend=backend)
    window.show()
    app.exec_()
