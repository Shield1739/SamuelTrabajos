from ttkthemes import ThemedTk

from parcial_turismo_v2 import controller


class App:
    def __init__(self, root=None):
        super(App, self).__init__()
        if root is None:
            root = ThemedTk(theme="radiance")
        self._root = root

        self._controllers = {}

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
            raise KeyError("No controller registrado: {}".format(nombre))
        return self.controllers[nombre]

    def add_controller(self, nombre, controller):
        if self.has_controller(nombre):
            raise KeyError("Controller ya existe: {}".format(nombre))
        self.controllers[nombre] = controller

    def remove_controller(self, nombre):
        if not self.has_controller(nombre):
            raise KeyError("Controller no existe: {}".format(nombre))
        self.controllers.pop(nombre)

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = controller.MainController()
    app.start()
