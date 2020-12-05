from ttkthemes import ThemedTk

from sem_shell_sort.controller import MainController, SubController
from sem_shell_sort.model import Model


class App:
    def __init__(self, root=None):
        super(App, self).__init__()

        if root is None:
            root = ThemedTk(theme="radiance")

        self._root = root
        self._controllers = {}

        # TODO Maybe store model here?
        self._model = Model()

    @property
    def root(self):
        return self._root

    @property
    def controllers(self):
        return self._controllers

    def has_controller(self, nombre):
        return nombre in self.controllers.keys()

    def get_controller(self, nombre):
        if not self.has_controller(nombre):
            raise KeyError("Controlador no registrado: {}".format(nombre))
        return self.controllers[nombre]

    def add_controller(self, name, controller):
        if self.has_controller(name):
            raise KeyError("Controlador ya registrado: {}".format(name))
        self.controllers[name] = controller

    def remove_controller(self, name):
        if not self.has_controller(name):
            raise KeyError("Controlador no registrado: {}".format(name))
        self.controllers.pop(name)

    @property
    def model(self):
        return self._model

    def start(self):
        self.preload()
        self.root.mainloop()

    def preload(self):
        self.root.title("Semestral - Shell Sorting")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.add_controller("main", MainController(parent=self, model=self.model))

    def load(self):
        self.root.geometry("1000x600")

        c = self.get_controller("main")

        self.add_controller("sub", SubController(parent=c.get_main_frame(), display_parent=c.get_display_frame(),
                                                 action_parent=c.get_action_frame(), model=self.model))
