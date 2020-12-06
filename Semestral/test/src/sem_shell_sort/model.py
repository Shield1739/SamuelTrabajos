from random import randint
from sem_shell_sort import Observable, SortState


class Model(Observable):
    def __init__(self):
        super(Model, self).__init__()
        self._ilist = []
        self.work_list = []
        self.generate_list()

        self._app_state = 1
        self._sort_state = SortState.NOT_STARTED

        self.gap = 0
        self.temp = 0
        self.j = 0
        self.k = 0

    @property
    def ilist(self):
        return self._ilist

    @ilist.setter
    def ilist(self, ilist):
        self._ilist = ilist

    @property
    def work_list(self):
        return self._work_list

    @work_list.setter
    def work_list(self, ilist):
        self._work_list = ilist

    def generate_list(self):
        # self.ilist = [4, 90, 7, 6, 64, 10, 23, 34, 12, 87]
        ilist = []
        size = randint(8, 12)
        while True:
            r = randint(1, 500)
            # if r not in ilist:
            ilist.append(r)
            if len(ilist) >= size:
                break

        self.ilist = ilist

    @property
    def app_state(self):
        return self._app_state

    @app_state.setter
    def app_state(self, app_state):
        self._app_state = app_state

    @property
    def sort_state(self):
        return self._sort_state

    @sort_state.setter
    @Observable.observed
    def sort_state(self, sort_state):
        self._sort_state = sort_state

    def shell_sort(self):
        self.work_list = self.ilist

        self.gap = len(self.work_list) // 2

        self.sort_state = SortState.SEARCHING

        while self.gap > 0:
            for i in range(self.gap, len(self.work_list)):
                self.temp = self.work_list[i]
                self.j = i
                self.k = self.j - self.gap
                self.sort_state = SortState.COMPARING

                if self.j >= self.gap and self.work_list[self.k] > self.temp:
                    while self.j >= self.gap and self.work_list[self.k] > self.temp:

                        if not self.sort_state == SortState.COMPARING:
                            self.sort_state = SortState.COMPARING

                        self.sort_state = SortState.COMPARE_FOUND

                        self.work_list[self.j] = self.work_list[self.k]
                        self.work_list[self.k] = self.temp
                        self.sort_state = SortState.FOUND_SWAP

                        self.sort_state = SortState.FOUND_OK
                        self.sort_state = SortState.FOUND_REDUCE
                        self.j -= self.gap
                        self.k = self.j - self.gap

                    self.work_list[self.j] = self.temp

                    self.j += self.gap
                    self.k = self.j - self.gap

                if self.sort_state == SortState.COMPARING:
                    self.sort_state = SortState.COMPARE_OK
                self.sort_state = SortState.COMPARE_DONE

            self.gap = self.gap // 2
            self.sort_state = SortState.REDUCING_GAP

        self.sort_state = SortState.SORTED
