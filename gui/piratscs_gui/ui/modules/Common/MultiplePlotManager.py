from piratscs_gui.ui.modules.Common.EventCounter import EventCounter
from piratscs_gui.ui.modules.Common.ColorsCreator import get_colors_list


class MultiplePlotManager():
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
