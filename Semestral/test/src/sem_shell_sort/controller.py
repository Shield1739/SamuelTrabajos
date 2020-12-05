from sem_shell_sort import Observer, SortState
from sem_shell_sort.view import MainView, DisplayView, ActionView
from sem_shell_sort.model import Model


class BaseController:
    def __init__(self, parent, model=None):
        super(BaseController, self).__init__()
        self._parent = parent
        self._model = model

    @property
    def parent(self):
        return self._parent

    @property
    def model(self):
        return self._model

    @property
    def root(self):
        return self.parent.root


class MainController(BaseController):
    def __init__(self, parent, model=None):
        super(MainController, self).__init__(parent=parent, model=model)

        self._view = MainView(self.root, self)

    @property
    def view(self):
        return self._view

    def load(self):
        self.parent.load()

    def get_main_frame(self):
        return self.view.get_widget("main_frame")

    def get_display_frame(self):
        return self.view.get_widget("display_frame")

    def get_action_frame(self):
        return self.view.get_widget("action_frame")

    def start_sorting(self):
        # TODO make enum for app state
        # self.model.app_state = Model.RUNNING
        self.model.shell_sort()


class SubController(BaseController, Observer):
    def __init__(self, parent, display_parent, action_parent, model=None):
        super(SubController, self).__init__(parent=parent, model=model)

        self.model.register_observer(self)
        self._display_view = DisplayView(display_parent, self)
        self._action_view = ActionView(action_parent, self)

    @property
    def display_view(self):
        return self._display_view

    @property
    def action_view(self):
        return self._action_view

    def get_ilist(self):
        return self.model.ilist

    def get_work_list(self):
        return self.model.work_list

    def update(self, observable):
        state = observable.sort_state
        k = observable.k
        j = observable.j

        if state == SortState.COMPARING:
            self.display_view.draw_comparing(k, j)
            self.action_view.draw_comparing(k, j)
        elif state == SortState.COMPARE_OK:
            self.display_view.draw_compare_ok(k, j)
            self.action_view.draw_compare_ok()
        elif state == SortState.COMPARE_DONE:
            self.display_view.draw_compare_done(k, j)
            self.action_view.draw_compare_done()
        elif state == SortState.COMPARE_FOUND:
            self.display_view.draw_compare_found(k, j)
            self.action_view.draw_compare_found()
        elif state == SortState.FOUND_SWAP:
            self.display_view.draw_found_swap(k, j)
            self.action_view.draw_found_swap()
        elif state == SortState.FOUND_OK:
            self.display_view.draw_found_ok(k, j)
            self.action_view.draw_found_ok(k, j)
        elif state == SortState.FOUND_REDUCE:
            self.display_view.draw_found_reduce(k, j)
            self.action_view.draw_found_reduce()
        elif state == SortState.SORTED:
            self.display_view.draw_sorted()
            self.action_view.draw_sorted()

        #self.parent.update()
        #self.parent.after(500)
