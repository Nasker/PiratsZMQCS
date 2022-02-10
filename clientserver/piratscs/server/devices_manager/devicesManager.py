from piratscs.logger import get_logger

from piratslib.controlNsensing.VoltageSense import VoltageSense
from piratslib.controlNsensing.WeightSense import WeightSense
from piratslib.controlNsensing.TemperatureSense import TemperatureSense
from piratslib.controlNsensing.DigitalOutputControl import DigitalOutputControl
from piratslib.controlNsensing.DigitalInputSense import DigitalInputSense
from pyvsr53dl.vsr53dl import PyVSR53DL

log = get_logger('Devices_Manager')

devices_list = ["temperature", "pressure", "weight", "voltage", "dig_in", "dig_out"]
N_DEV_MEASUREMENT = 4

class DevicesManager:
    def __init__(self):
        log.debug('Initializing Module Pirats Voltage')
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

    @property
    def temperature_channels(self):
        return self._temp_channels_list
    @temperature_channels.setter
    def temperature_channels(self, channels_list):
        self._temp_channels_list = channels_list

    @property
    def voltage_channels(self):
        return self._voltage_channels_list
    @voltage_channels.setter
    def voltage_channels(self, channels_list):
        self._voltage_channels_list = channels_list

    @property
    def weight_channels(self):
        return self._weight_channels_list
    @weight_channels.setter
    def weight_channels(self, channels_list):
        self._weight_channels_list = channels_list

    @property
    def pressure_channels(self):
        return self._pressure_channels_list
    @pressure_channels.setter
    def pressure_channels(self, channels_list):
        self._pressure_channels_list = channels_list

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
