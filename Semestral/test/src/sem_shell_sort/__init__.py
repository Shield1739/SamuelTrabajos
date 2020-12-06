import functools
from enum import Enum


class AppState(Enum):
    CONFIGURING = 0
    LOADED = 1
    RUNNING = 2
    PAUSED = 3
    STOPPED = 4
    FINISHED = 5


class SortState(Enum):
    NOT_STARTED = "NOT STARTED"
    SORTED = "SORTED"
    SEARCHING = "SEARCHING"
    COMPARING = "COMPARING"
    COMPARE_OK = "COMPARE OK"
    COMPARE_DONE = "COMPARE DONE"
    COMPARE_FOUND = "COMPARE FOUND"
    FOUND_SWAP = "FOUND SWAP"
    FOUND_OK = "FOUND OK"
    FOUND_REDUCE = "FOUND REDUCE"
    REDUCING_GAP = "REDUCING GAP"


class Observer(object):
    def __init__(self):
        super(Observer, self).__init__()

    def update(self, observable):
        raise NotImplementedError


class Observable(object):
    def __init__(self):
        super(Observable, self).__init__()
        self._observers = []

    def register_observer(self, observer):
        if not isinstance(observer, Observer):
            raise ValueError("No es un observer {}".format(type(observer)))
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def observed(f):
        @functools.wraps(f)
        def magic(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            self.notify_observers()
            return result

        return magic

    observed = staticmethod(observed)
