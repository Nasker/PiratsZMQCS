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
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from simplecs_gui.system.logger import get_logger
from simplecs_gui.ui.modules.module import Module
from simplecs_gui.ui.modules.daq_connection.mini_daq_conn_ui import Ui_mini_daq_connection
from simplecs_gui.ui.modules.daq_connection.daq_conn_details_ui import Ui_daq_connection_details

import datetime
import pprint

log = get_logger('mod_connection')


class MiniDaqConn(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._setup_ui()

    def _setup_ui(self):
        self._ui = Ui_mini_daq_connection()
        self._ui.setupUi(self)
        self._ui.ip_lineedit.setText(self._parent.conf.server_comm.ip)
        self._ui.pb_daq_connect.clicked.connect(self._connect_be)
        self._ui.pb_conn_details.clicked.connect(self._module.show_conn_details)

        self._ui.pb_daq_connect.setEnabled(not self._module.connected)

        self._parent.backend.signaler.sign_be_comm_client_connected.connect(self._connected)

    def _connected(self, isconn):
        self._ui.pb_daq_connect.setEnabled(not isconn)

    def _connect_be(self):
        ip = self._ui.ip_lineedit.text()
        self._module.connect_be(ip=ip)

    def update_ip(self, ip):
        self._ui.ip_lineedit.setText(ip)


class DaqConnDetails(QWidget):
    def __init__(self, module):
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._setup_ui()

    def _update_asyncs_contents_client(self):
        be = self._parent.backend
        stats = be.async_exec.stats()
        table = self._ui.tbl_asyncs_client
        table.setRowCount(0)
        labels = sorted(stats.keys())
        for label in labels:
            r = table.rowCount()
            table.insertRow(r)
            if isinstance(label, str):
                table.setItem(r, 0, QTableWidgetItem(label))
            elif isinstance(label, bytes):
                table.setItem(r, 0, QTableWidgetItem(label.decode('utf-8')))
            else:
                table.setItem(r, 0, QTableWidgetItem(str(label)))
            table.setItem(r, 1, QTableWidgetItem(str(stats[label])))
        table.resizeColumnsToContents()

    def _update_asyncs_contents_server(self):
        be = self._parent.backend
        ser_stats_ans = None
        try:
            ser_stats_ans = be.comm_client.get_server_pub_stats()
        except:
            log.exception('Error when asking for server stats')
        else:
            # log.info(f"Answer from server type: {ser_stats_ans}. As dict:{ser_stats_ans.as_dict}")
            if ser_stats_ans.ans is not None:
                table = self._ui.tbl_asyncs_server
                table.setRowCount(0)
                stats = ser_stats_ans.ans
                labels = sorted(stats.keys())
                for label in labels:
                    r = table.rowCount()
                    table.insertRow(r)
                    if isinstance(label, str):
                        table.setItem(r, 0, QTableWidgetItem(label))
                    elif isinstance(label, bytes):
                        table.setItem(r, 0, QTableWidgetItem(label.decode('utf-8')))
                    else:
                        table.setItem(r, 0, QTableWidgetItem(str(label)))
                    for i, v in enumerate(['total_pub', '1min', '5min', '15min', '30min', '60min']):
                        table.setItem(r, 1+i, QTableWidgetItem(str(stats[label].get(v, ''))))
                table.resizeColumnsToContents()
                log.debug(f'Received stats from server: {stats}')


    def _setup_ui(self):
        self._ui = Ui_daq_connection_details()
        self._ui.setupUi(self)
        self._ui.ip_lineedit.setText(self._parent.conf.server_comm.ip)
        self._ui.pb_daq_connect.clicked.connect(self._connect_be)
        self._ui.btnUpdateClient.clicked.connect(self._update_asyncs_contents_client)
        self._ui.btnUpdateServer.clicked.connect(self._update_asyncs_contents_server)
        self._ui.tbl_asyncs_client.setColumnCount(2)
        self._ui.tbl_asyncs_client.setHorizontalHeaderLabels(['Async Name', 'Received'])
        self._ui.tbl_asyncs_client.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self._ui.tbl_asyncs_server.setColumnCount(7)
        self._ui.tbl_asyncs_server.setHorizontalHeaderLabels(['Async Name', 'Sent total', '< 1min', "< 5min", '< 15min',
                                                              '< 30min', '< 60min'])
        self._ui.tbl_asyncs_server.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        self._ui.pb_daq_connect.setEnabled(not self._module.connected)
        self._ui.btnUpdateClient.setEnabled(self._module.connected)
        self._ui.btnUpdateServer.setEnabled(self._module.connected)
        self._parent.backend.signaler.sign_be_comm_client_connected.connect(self._connected)
        self._parent.backend.signaler.sign_be_comm_async_app_cmd.connect(self._new_cmd_async)

    def _connected(self, isconn):
        self._ui.pb_daq_connect.setEnabled(not isconn)
        self._ui.btnUpdateClient.setEnabled(isconn)
        self._ui.btnUpdateServer.setEnabled(isconn)

    def _connect_be(self):
        ip = self._ui.ip_lineedit.text()
        self._module.connect_be(ip=ip)

    def update_ip(self, ip):
        self._ui.ip_lineedit.setText(ip)

    def _new_cmd_async(self, cmd_async):
        txt = f'Received CMD async on {datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}\n\n'
        txt += pprint.pformat(cmd_async.as_dict)
        self._ui.txt_last_async_cmd.setText(txt)


class DaqConnModule(Module):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = MiniDaqConn(module=self)
        self._widget = None
        self._setup()

    @property
    def parent(self):
        return self._parent

    def show_conn_details(self):
        if self._widget is None:
            self._widget = DaqConnDetails(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()

    def _setup(self):
        pass

    def connect_be(self, ip):
        ip = str(ip)
        self._miniwidget.update_ip(ip)
        if self._widget is not None:
            self._widget.update_ip(ip)
        self._parent.conf.server_comm.ip = ip
        self._parent.conf.save_as_yaml()
        try:
            self._parent.backend.connect_to_server(ip=ip,
                                                   req_port=self._parent.conf.server_comm.cmd_port,
                                                   async_port=self._parent.conf.server_comm.async_port)
        except:
            log.exception('Failed to connect')
        else:
            self.connected = True
