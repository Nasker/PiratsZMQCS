from piratscs.logger import get_logger

from piratslib.controlNsensing.VoltageSense import VoltageSense
from piratslib.controlNsensing.WeightSense import WeightSense
from piratslib.controlNsensing.TemperatureSense import TemperatureSense
from piratslib.controlNsensing.DigitalOutputControl import DigitalOutputControl
from piratslib.controlNsensing.DigitalInputSense import DigitalInputSense
from pyvsr53dl.vsr53dl import PyVSR53DL

log = get_logger('Devices_Manager')

devices_list = ["temperature", "pressure", "weight", "voltage", "dig_in", "dig_out"]
devices_dict = {"temperature":0, "pressure":1, "weight":2, "voltage":3, "dig_in":4, "dig_out":5}
N_DEV_MEASUREMENT = 4

class DevicesManager:
    def __init__(self):
        log.debug('Initializing Module Pirats Voltage')
        self._current_devices_list = [0, 1, 2, 3]
        self._pirats_temperature_sense = None
        self._pressure_sense = None
        self._pirats_weight_sense = None
        self._pirats_voltage_sense = None
        self._pirats_in_sense = None
        self._pirats_out_control = None

        self._temp_channels_list = []
        self._voltage_channels_list = []
        self._weight_channels_list = []
        self._pressure_channels_list = []
        self._init_devices()

    def _init_devices(self):
        self._init_voltage_sense()
        self._init_weight_sense()
        self._init_temperature_sense()
        self._init_pressure_sense()
        self._init_inout()

    def _init_temperature_sense(self):
        self._pirats_temperature_sense = TemperatureSense()

    def _init_voltage_sense(self):
        self._pirats_voltage_sense = VoltageSense()

    def _init_weight_sense(self):
        NOMINAL_LOAD = 10000
        NOMINAL_OUTPUT = 0.002
        FULL_SCALE_VOLT = 5.0
        self._pirats_weight_sense = WeightSense(NOMINAL_LOAD, NOMINAL_OUTPUT, FULL_SCALE_VOLT)

    def _init_pressure_sense(self):
        from pyvsr53dl.sys import dev_tty
        sensor_address = 1
        self._pressure_sense = PyVSR53DL(dev_tty, sensor_address)
        self._pressure_sense.open_communication()
        self._pressure_sense.get_device_type()

    def _init_inout(self):
        self._pirats_in_sense = DigitalInputSense()
        self._pirats_out_control = DigitalOutputControl()

    def compose_measurements_dict(self):
        measurements_dict = {}
        for device in self._current_devices_list:
            if device == devices_dict["temperature"]:
                measurements_dict[devices_dict["temperature"]] = self._temp_channels_list
            elif device == devices_dict["pressure"]:
                measurements_dict[devices_dict["pressure"]] = self._pressure_channels_list
            elif device == devices_dict["weight"]:
                measurements_dict[devices_dict["weight"]] = self._weight_channels_list
            elif device == devices_dict["voltage"]:
                measurements_dict[devices_dict["voltage"]] = self._voltage_channels_list
        log.debug('Composing Measurements Dict: {}'.format(measurements_dict))
        return measurements_dict

    def compose_measurements_header(self):
        measurements_dict = self.compose_measurements_dict()
        measurements_header = []
        for measurement_type in measurements_dict:
            for channel in measurements_dict[measurement_type]:
                measurements_header.append(f'{devices_list[measurement_type]}_ch{channel}')
        log.debug('Composing Measurements Header: {}'.format(measurements_header))
        return measurements_header

    @property
    def current_devices_list(self):
        return self._current_devices_list
    @current_devices_list.setter
    def current_devices_list(self, current_devices_list):
        self._current_devices_list = current_devices_list

    @property
    def temperature_channels(self):
        return self._temp_channels_list
    @temperature_channels.setter
    def temperature_channels(self, channels_list):
        self._temp_channels_list = channels_list
        self.compose_measurements_header()

    @property
    def voltage_channels(self):
        return self._voltage_channels_list
    @voltage_channels.setter
    def voltage_channels(self, channels_list):
        self._voltage_channels_list = channels_list
        self.compose_measurements_header()

    @property
    def weight_channels(self):
        return self._weight_channels_list
    @weight_channels.setter
    def weight_channels(self, channels_list):
        self._weight_channels_list = channels_list
        self.compose_measurements_header()

    @property
    def pressure_channels(self):
        return self._pressure_channels_list
    @pressure_channels.setter
    def pressure_channels(self, channels_list):
        self._pressure_channels_list = channels_list
        self.compose_measurements_header()

    def get_temperature_readings(self):
        return self._pirats_temperature_sense.get_temps_list(self._temp_channels_list)

    def get_voltage_readings(self):
        return self._pirats_voltage_sense.get_voltages_list(self._voltage_channels_list)

    def get_weight_readings(self):
        return self._pirats_weight_sense.get_weights_list(self._weight_channels_list)

    def get_pressure_readings(self):
        return [{0: self._pressure_sense.get_measurement_value()}]

    def get_inputs_state(self):
        return self._pirats_in_sense.digital_read_all()

    def set_output_state(self, output, state):
        self._pirats_out_control.digital_write(output, state)
