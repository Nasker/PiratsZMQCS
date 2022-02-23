from piratscs_gui.ui.modules.Common.EventCounter import EventCounter
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list


class MultiplePlotManager():
    devices_dict = {"temperature": 0, "pressure": 1, "weight": 2, "voltage": 3, "dig_in": 4, "dig_out": 5}
    def __init__(self):
        self._plots_dict = {0:[], 1:[], 2:[], 3:[]}
        self._events_list_dict = {0:[], 1:[], 2:[], 3:[]}
        for i in self._plots_dict:
            self._events_list_dict[i].append(EventCounter())

    def set_plot(self, device_id, plot):
        self._plots_dict[device_id] = plot

    def get_plot(self, device_id):
        return self._plots_dict[device_id]

    def set_events_list(self, device_id, events_list):
        self._events_list_dict[device_id] = events_list

    def get_events_list(self, device_id):
        return self._events_list_dict[device_id]

    def reset_channels(self, device_id, created_channels, plot_ref):
        self.get_plot(device_id).clear()
        self.set_plot(device_id, [plot_ref for _ in range(0, created_channels)])
        self.get_events_list(device_id).clear()
        self.set_events_list(device_id, [EventCounter() for _ in range(0, created_channels)])