from ttkthemes import ThemedTk

from parcial_turismo_v2.data import Cliente
from parcial_turismo_v2.model import Model
from parcial_turismo_v2.view import *


class BaseController:
    def __init__(self, root):
        super(BaseController, self).__init__()
        self._root = root
        self._model = Model()

        self._active_view = None

    @property
    def root(self):
        return self._root

    @property
    def model(self):
        return self._model

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, active_view):
        self._active_view = active_view

    def destroy_active_view(self):
        if self.active_view is not None:
            self.active_view.frame.destroy()
            self.active_view = None

    def start(self):
        self.root.mainloop()


class MainController(BaseController):
    def __init__(self):
        super().__init__(ThemedTk(theme="radiance"))
        self.root.title("Parcial & Proyecto #1")
        self.root.resizable(False, False)

        self.create_presentacion_view()

    # TODO VIEW SWITCHER
    # Create views
    def create_presentacion_view(self):
        self.destroy_active_view()
        self.active_view = PresentacionWindowView(self.root, self)

    def create_mapa_view(self):
        self.destroy_active_view()
        self.active_view = MapaWindowView(self.root, self)

    def create_select_view(self):
        self.destroy_active_view()
        self.active_view = SelectWindowView(self.root, self)

    def create_reservar_view(self):
        self.destroy_active_view()
        self.active_view = ReservarWindowView(self.root, self)

    def create_pagar_view(self):
        self.destroy_active_view()
        self.active_view = PagarWindowView(self.root, self)

    # funcs
    def update_act_vars(self):
        subtotal = self.get_obj_act(Tipos.ZONA).precio * float(self.get_var_act(Tipos.PERSONAS))
        self.set_var_act(Tipos.SUBTOTAL, subtotal)

        descuento = 0
        if self.get_var_act(Tipos.JUBILADO):
            descuento += 0.10

        if self.get_var_act(Tipos.PERSONAS) >= 3:
            descuento += 0.15

        if subtotal > 2000:
            descuento += 0.05

        descuento = subtotal * descuento
        self.set_var_act(Tipos.DESCUENTO, descuento)

    # Getters/Setters
    def set_region_act_by_nombre(self, nombre_region):
        if nombre_region == "":
            return None

        for i in self.model.regiones:
            if i.nombre.lower() == nombre_region.lower():
                self.set_obj_act(Tipos.REGION, i)
                return

    def set_new_cliente_act(self, v):
        j = self.get_var_act(Tipos.JUBILADO)
        cliente = Cliente(v["Nombre:"].get(), v["Cedula:"].get(), v["Edad:"].get(), v["Sexo:"].get(),
                          v["Nacionalidad:"]
                          .get(), v["Telefono:"].get(), j)

        self.set_obj_act(Tipos.CLIENTE, cliente)

    def add_reserva(self):
        self.model.add_reserva()

    def set_obj_act(self, tipo, obj):
        self.model.set_active_objs(tipo, obj)

    def get_obj_act(self, tipo):
        return self.model.get_active_objs(tipo)

    def set_var_act(self, tipo, var):
        self.model.set_active_vars(tipo, var)

    def get_var_act(self, tipo):
        return self.model.get_active_vars(tipo)

    def get_reservalist(self):
        return self.model.reserva_list

    def clear_reservalist(self):
        self.model.reserva_list.clear()
        self.set_obj_act(Tipos.CLIENTE, None)

    def pop_reserva(self, index):
        self.model.reserva_list.pop(index)
