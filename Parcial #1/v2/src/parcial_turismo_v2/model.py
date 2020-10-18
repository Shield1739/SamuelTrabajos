from parcial_turismo_v2.data import Reserva
from parcial_turismo_v2 import Tipos, get_regiones_list


class Model:
    def __init__(self):
        self._regiones = get_regiones_list()

        self._active_objs = {}

        self.active_objs[Tipos.REGION] = None
        self.active_objs[Tipos.ZONA] = None
        self.active_objs[Tipos.CLIENTE] = None

        self._active_vars = {}

        self.active_vars[Tipos.PERSONAS] = 1
        self.active_vars[Tipos.SUBTOTAL] = 0.0
        self.active_vars[Tipos.DESCUENTO] = 0.0
        self.active_vars[Tipos.JUBILADO] = False

        self._reserva_list = []

    @property
    def regiones(self):
        return self._regiones

    @property
    def active_objs(self):
        return self._active_objs

    def has_active_objs(self, nombre):
        return nombre in self.active_objs.keys()

    def get_active_objs(self, nombre):
        if not self.has_active_objs(nombre):
            raise KeyError("Obj Activo no existe")
        return self.active_objs[nombre]

    def set_active_objs(self, nombre, obj):
        if not self.has_active_objs(nombre):
            raise KeyError("Obj Activo no existe")
        self.active_objs[nombre] = obj
        return obj

    @property
    def active_vars(self):
        return self._active_vars

    def has_active_vars(self, nombre):
        return nombre in self.active_vars.keys()

    def get_active_vars(self, nombre):
        if not self.has_active_vars(nombre):
            raise KeyError("Obj Activo no existe")
        return self.active_vars[nombre]

    def set_active_vars(self, nombre, var):
        if not self.has_active_vars(nombre):
            raise KeyError("Obj Activo no existe")
        self.active_vars[nombre] = var
        return var

    @property
    def reserva_list(self):
        return self._reserva_list

    @reserva_list.setter
    def reserva_list(self, reserva):
        self._reserva_list.append(reserva)

    def add_reserva(self):
        region = self.active_objs[Tipos.REGION]
        zona = self.active_objs[Tipos.ZONA]
        cantidad = self.active_vars[Tipos.PERSONAS]
        subtotal = self.active_vars[Tipos.SUBTOTAL]
        descuento = self.active_vars[Tipos.DESCUENTO]

        r = Reserva(region.nombre, region.get_tipo_nombre(), zona, cantidad, subtotal, descuento)

        self.reserva_list = r

        self.active_objs[Tipos.REGION] = None
        self.active_objs[Tipos.ZONA] = None

        self.active_vars[Tipos.PERSONAS] = 1
        self.active_vars[Tipos.SUBTOTAL] = 0.0
        self.active_vars[Tipos.DESCUENTO] = 0.0
        self.active_vars[Tipos.JUBILADO] = False
