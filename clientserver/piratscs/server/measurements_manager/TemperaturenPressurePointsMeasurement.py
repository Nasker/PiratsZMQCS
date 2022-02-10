import csv
import time
from datetime import datetime
import numpy as np

MEASUREMENT_PERIOD_SEC = 1

def _to_kelvin(celsius_value):
    return round(celsius_value + 273.15, 3)

def _now_timestamp_str():
    return datetime.fromtimestamp(time.time()).strftime("%d%m%Y_%H%M%S")

def _now_time_n_date_stamp_str():
    time_stamp = time.time()
    time_str = datetime.fromtimestamp(time_stamp).strftime("%H:%M:%S")
    date_str = datetime.fromtimestamp(time_stamp).strftime("%d/%m/%Y")
    return [date_str, time_str]

def _create_measurements_file(n_pressure_points, n_temp_points):
    date_time = _now_timestamp_str()
    file_name = f'measurements/FCC_{n_pressure_points}_pressure_points_{n_temp_points}_temp_points_{date_time}.csv'
    with open(file_name, 'w', newline='') as file:
        dataset_writer = csv.writer(file)
        header_list = ["date", "time", "pressure", "ambient_temp", "ss_plate_temp", "top_temp", "cold_sink_temp"]
        log.info(f'Writing measurements file header: {header_list}')
        dataset_writer.writerow(header_list)
    return file_name

def _write_measurement(file_name, dataset):
    with open(file_name, 'a', newline='') as file:
        dataset_writer = csv.writer(file)
        dataset_writer.writerow(dataset)

def main_measurement_routine(n_pressure_points, n_temp_points):
    log.info("Opening communication with temperature sensors.")
    temp_sense = TemperatureSense()
    log.info("Opening communication with pressure sensor.")
    sensor_address = 1
    vacuum_sense = PyVSR53DL(dev_tty, sensor_address)
    vacuum_sense.open_communication()
    vacuum_sense.get_device_type()
    vacuum_sense.get_product_name()
    log.info("Opening measurement files.")
    file_name = create_measurements_file(n_pressure_points, n_temp_points)
    log.info(f'File Name is: {file_name}')
    log.info(f"Starting measurements on {n_pressure_points} pressure points and {n_temp_points} temperature points")
    last_time = time.time()
    i = 0
    measurements_collector = [np.zeros(0) for _ in range(n_temp_points)]
    try:
        while True:
            for n, array in enumerate(measurements_collector):
                measurements_collector[n] = np.append(array, temp_sense.get_temp(n))
            if time.time() > last_time + MEASUREMENT_PERIOD_SEC:
                for n, array in enumerate(measurements_collector):
                    measurements_collector[n] = np.mean(array)
                dataset = _now_time_n_date_stamp_str()
                dataset.append(vacuum_sense.get_measurement_value())
                dataset.extend([_to_kelvin(measurements_collector[x]) for x in range(n_temp_points)])
                log.info(f'#{i+1}: {dataset}')
                _write_measurement(file_name, dataset)
                i += 1
                last_time = time.time()
                measurements_collector = [np.zeros(0) for _ in range(n_temp_points)]
            time.sleep(0.1)
