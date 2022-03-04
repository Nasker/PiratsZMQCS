""" GUI for the Example module

"""
__author__ = 'Oscar Martinez'
__copyright__ = 'Copyleft 2022'
__date__ = '4/2/22'
__credits__ = ['Otger Ballester', 'Oscar Martinez']
__license__ = 'CC0 1.0 Universal'
__version__ = '0.1'
__maintainer__ = 'Oscar Martinez'
__email__ = 'omartinez@ifae.es'

import os
import datetime
from PyQt5.QtWidgets import QWidget, QAction
from PyQt5.QtGui import QIcon
from piratscs_gui.system.logger import get_logger
from piratscs_gui.ui.modules.module import Module

from piratscs_gui.ui.modules.modmeasurements.modmeasurements_big_ui import Ui_ModuleMeasurementsBig
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list
from piratscs_gui.ui.modules.Common.MultiplePlotManager import MultiplePlotManager

log = get_logger('modmeasurements_gui')

N_CHANNELS = 4
N_ROWS = 2
N_COLS = int(N_CHANNELS / N_ROWS)
colors = get_colors_list(N_CHANNELS)


class ModMeasurementsBigWidget(QWidget):
    def __init__(self, module):
        self._temp_device_id = MultiplePlotManager.devices_dict["temperature"]
        self._pressure_device_id = MultiplePlotManager.devices_dict["pressure"]
        self._weight_device_id = MultiplePlotManager.devices_dict["weight"]
        self._voltage_device_id = MultiplePlotManager.devices_dict["voltage"]
        self._module = module
        self._parent = module.parent
        super().__init__(self._parent)
        self._plot_man = MultiplePlotManager()
        self._setup_ui()
        self._default_label_style_sheet = self._ui.lbl_set_channel_recvd.styleSheet()

    def _set_measurements(self):
        value = self._ui.ledit_measurement_set.text()
        log.debug(f"Setting measurements to {value}")
        ret_val = self._parent.backend.comm_client.modmeasurements.select_measurements(value)
        log.debug(f"Received answer for  command: '{ret_val.as_dict}'")
        if ret_val.error:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.error))
            self._ui.lbl_set_channel_recvd.setStyleSheet("color: red")
        else:
            self._ui.lbl_set_channel_recvd.setText(str(ret_val.ans))
            self._ui.lbl_set_channel_recvd.setStyleSheet(self._default_label_style_sheet)
        self._ui.lbl_set_channel_recvd_on.setText(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S"))

        self._selected_devices_channels = \
            self._parent.backend.comm_client.modmeasurements.get_select_devices_channels().as_dict['contents']['ans']
        log.debug(f"Selected devices and channels: {self._selected_devices_channels}")
        if f'{self._temp_device_id}' in self._selected_devices_channels:
            temp_created_channels = len(self._selected_devices_channels[f'{self._temp_device_id}'])
            self._plot_man.get_plot(self._temp_device_id).clear()
            self._plot_man.set_plot(self._temp_device_id,
                                    [self._ui.tempGraph.plot() for _ in range(0, temp_created_channels)])
            self._plot_man.reset_channels(self._temp_device_id, temp_created_channels, self._ui.tempGraph.plot())

        if f'{self._pressure_device_id}' in self._selected_devices_channels:
            pressure_created_channels = len(self._selected_devices_channels[f'{self._pressure_device_id}'])
            self._plot_man.get_plot(self._pressure_device_id).clear()
            self._plot_man.set_plot(self._pressure_device_id,
                                    [self._ui.pressureGraph.plot() for _ in range(0, pressure_created_channels)])
            self._plot_man.reset_channels(self._pressure_device_id, pressure_created_channels,
                                          self._ui.pressureGraph.plot())

        if f'{self._weight_device_id}' in self._selected_devices_channels:
            weight_created_channels = len(self._selected_devices_channels[f'{self._weight_device_id}'])
            self._plot_man.get_plot(self._weight_device_id).clear()
            self._plot_man.set_plot(self._weight_device_id,
                                    [self._ui.weightGraph.plot() for _ in range(0, weight_created_channels)])
            self._plot_man.reset_channels(self._weight_device_id, weight_created_channels, self._ui.weightGraph.plot())

        if f'{self._voltage_device_id}' in self._selected_devices_channels:
            voltage_created_channels = len(self._selected_devices_channels[f'{self._voltage_device_id}'])
            self._plot_man.get_plot(self._voltage_device_id).clear()
            self._plot_man.set_plot(self._voltage_device_id,
                                    [self._ui.voltageGraph.plot() for _ in range(0, voltage_created_channels)])
            self._plot_man.reset_channels(self._voltage_device_id, voltage_created_channels,
                                          self._ui.voltageGraph.plot())

    def _set_period(self):
        value = self._ui.spin_period_set.value() / 1000.0
        self._parent.backend.comm_client.modmeasurements.set_period(value)
        log.debug(f"Setting period to {value}")

    def _start_acq(self):
        log.debug(f'Filename: {self._ui.ledit_filename_set.text()}')
        self._parent.backend.comm_client.modmeasurements.set_file_name(self._ui.ledit_filename_set.text())
        self._parent.backend.comm_client.modmeasurements.start_acq()
        log.debug("Started voltage acquisition")

    def _stop_acq(self):
        self._parent.backend.comm_client.modmeasurements.stop_acq()
        log.debug("Stopped voltage acquisition")

    def _clear_chart(self):
        self._ui.tempGraph.clear()
        self._ui.pressureGraph.clear()
        self._ui.weightGraph.clear()
        self._ui.voltageGraph.clear()
        log.debug("Clearing charts")

    def _recvd_measurements(self, async_msg):
        last_measurement_text = f"{async_msg.as_dict['contents']['topic']} : "
        last_measurement_text += f"{async_msg.as_dict['contents']['value']}"
        self._ui.lbl_last_measurement.setText(last_measurement_text)
        if async_msg.as_dict['contents']['topic'] == 'measurement_temp':
            self.process_temp_async(async_msg.as_dict['contents']['value'])
        elif async_msg.as_dict['contents']['topic'] == 'measurement_pressure':
            self.process_pressure_async(async_msg.as_dict['contents']['value'])
        elif async_msg.as_dict['contents']['topic'] == 'measurement_weight':
            self.process_weight_async(async_msg.as_dict['contents']['value'])
        elif async_msg.as_dict['contents']['topic'] == 'measurement_voltage':
            self.process_voltage_async(async_msg.as_dict['contents']['value'])

    def process_temp_async(self, async_dict):
        temp_list = async_dict
        for n, temp_dict in enumerate(temp_list):
            for key, value in temp_dict.items():
                self._plot_man.get_events_list(self._temp_device_id)[n].new_event(value)
                x, y = self._plot_man.get_events_list(self._temp_device_id)[n].averages_chart_data
                self._plot_man.get_plot(self._temp_device_id)[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        log.debug(f"Received temperature: {async_dict}")

    def process_pressure_async(self, async_dict):
        pressure_list = async_dict
        for n, pressure_dict in enumerate(pressure_list):
            for key, value in pressure_dict.items():
                self._plot_man.get_events_list(self._pressure_device_id)[n].new_event(value)
                x, y = self._plot_man.get_events_list(self._pressure_device_id)[n].averages_chart_data
                self._plot_man.get_plot(self._pressure_device_id)[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        log.debug(f"Received pressure: {async_dict}")

    def process_weight_async(self, async_dict):
        weight_list = async_dict
        for n, weight_dict in enumerate(weight_list):
            for key, value in weight_dict.items():
                self._plot_man.get_events_list(self._weight_device_id)[n].new_event(value)
                x, y = self._plot_man.get_events_list(self._weight_device_id)[n].averages_chart_data
                self._plot_man.get_plot(self._weight_device_id)[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        log.debug(f"Received weight: {async_dict}")

    def process_voltage_async(self, async_dict):
        voltage_list = async_dict
        for n, voltage_dict in enumerate(voltage_list):
            for key, value in voltage_dict.items():
                self._plot_man.get_events_list(self._voltage_device_id)[n].new_event(value)
                x, y = self._plot_man.get_events_list(self._voltage_device_id)[n].averages_chart_data
                self._plot_man.get_plot(self._voltage_device_id)[n].setData(x=x, y=y, pen=colors[int(key)], thickness=3)
        log.debug(f"Received voltage: {async_dict}")

    def _setup_ui(self):
        self._ui = Ui_ModuleMeasurementsBig()
        self._ui.setupUi(self)
        self._ui.start_acq_btn.clicked.connect(self._start_acq)
        self._ui.stop_acq_btn.clicked.connect(self._stop_acq)
        self._ui.measTempCheckBox.stateChanged.connect(self.print_selected_measurements_ledit)
        self._ui.measVoltageCheckBox.stateChanged.connect(self.print_selected_measurements_ledit)
        self._ui.measPressureCheckBox.stateChanged.connect(self.print_selected_measurements_ledit)
        self._ui.measWeightCheckBox.stateChanged.connect(self.print_selected_measurements_ledit)
        self._ui.pb_measurement_set.clicked.connect(self._set_measurements)
        self._ui.pb_period_set.clicked.connect(self._set_period)
        self._ui.btn_clear_chart.clicked.connect(self._clear_chart)
        self._parent.backend.signaler.sign_be_comm_async_measurement_temp.connect(self._recvd_measurements)
        self._parent.backend.signaler.sign_be_comm_async_measurement_pressure.connect(self._recvd_measurements)
        self._parent.backend.signaler.sign_be_comm_async_measurement_weight.connect(self._recvd_measurements)
        self._parent.backend.signaler.sign_be_comm_async_measurement_voltage.connect(self._recvd_measurements)

    def print_selected_measurements_ledit(self):
        active_channels = []
        for j in range(N_ROWS):
            for i in range(N_COLS):
                if self._ui.gridLayout.itemAtPosition(j, i).widget().isChecked():
                    active_channels.append(i + j * N_COLS)
        self._ui.ledit_measurement_set.setText(",".join(str(x) for x in active_channels))


class ModMeasurementsModule(Module):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.connected = False
        self._miniwidget = None  # miniwidgets are the ones that goes to the column
        self._widget = None
        self._action = self._set_action()

    def _set_action(self):
        dirname = os.path.dirname(os.path.abspath(__file__))
        ico_path = os.path.join(dirname, 'media', 'measurements_ico.png')
        action = QAction(QIcon(ico_path), "Pirats Measurement", self._parent)
        action.setStatusTip("Open Pirats Measurement widget")
        action.triggered.connect(self.show_modmeasurements)
        return action

    def action_function(self):
        self._widget.show()

    @property
    def parent(self):
        return self._parent

    def show_modmeasurements(self):
        if self._widget is None:
            self._widget = ModMeasurementsBigWidget(module=self)
            print("adding sub window to mdi")
            self._parent.central.addSubWindow(self._widget)
        self._widget.show()
