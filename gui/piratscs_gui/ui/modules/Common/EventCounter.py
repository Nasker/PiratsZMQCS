from functools import reduce
import datetime

class EventCounter:
    def __init__(self, interval=60):
        self._events = []
        self._interval = interval
        self._avgs = []
        self._avgs_ts = []

    def new_event(self, value):
        now = self.now
        self._events.append((value, now))
        self._clean()
        self._avgs.append(self._avg())
        self._avgs_ts.append(now)

    @property
    def now(self):
        return datetime.datetime.utcnow().timestamp()

    @property
    def threshold(self):
        return self.now - self._interval

    def _clean(self):
        th = self.threshold
        self._events = [x for x in self._events if x[1] > th]
        self._avgs_ts = [x for x in self._avgs_ts if x > th]
        self._avgs = self._avgs[-len(self._avgs_ts):]

    @property
    def avg(self):
        return self._avgs[-1]

    def _avg(self):
        lst = [x[0] for x in self._events]
        return reduce(lambda a, b: a + b, lst) / len(lst)

    @property
    def len(self):
        return len(self._events)

    @property
    def averages_chart_data(self):
        return self._avgs_ts, self._avgs

