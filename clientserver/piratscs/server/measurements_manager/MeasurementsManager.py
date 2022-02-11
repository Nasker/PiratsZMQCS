import csv
import time
from datetime import datetime
import numpy as np
from piratscs.logger import get_logger

log = get_logger('Measurements_Manager')

class MeasurementsManager:
    """
    This class is responsible for managing the measurements.
    """
    def __init__(self, filename=None):
        self._filename = filename
        self.dataset_count = 0

    def create_measurements_file(self, filename=None, measurements_list=None):
        self.dataset_count = 0
        date_time = self._now_timestamp_str()
        if filename is None or filename == '':
            self._filename = f'../measurements/{date_time}_measurements.csv'
        else:
            self._filename = f'../measurements/{filename}.csv'
        with open(self._filename, 'w', newline='') as file:
            dataset_writer = csv.writer(file)
            header = ["date", "time"]
            header_list  = header + measurements_list
            log.info(f'Writing measurements file header: {header_list}')
            dataset_writer.writerow(header_list)

    def append_measurement_dataset(self, data):
        dataset = self._now_time_stamp_list()
        dataset.append(data)
        self.dataset_count += 1
        log.info(f'#{self.dataset_count}: {dataset}')
        self._write_measurement(dataset)

    def _write_measurement(self, dataset):
        with open(self._filename, 'a', newline='') as file:
            dataset_writer = csv.writer(file)
            dataset_writer.writerow(dataset)

    @staticmethod
    def _to_kelvin(celsius_value):
        return round(celsius_value + 273.15, 3)

    @staticmethod
    def _now_timestamp_str():
        return datetime.fromtimestamp(time.time()).strftime("%d%m%Y_%H%M%S")

    @staticmethod
    def _now_time_stamp_list():
        time_stamp = time.time()
        time_str = datetime.fromtimestamp(time_stamp).strftime("%H:%M:%S")
        date_str = datetime.fromtimestamp(time_stamp).strftime("%d/%m/%Y")
        return [date_str, time_str]
