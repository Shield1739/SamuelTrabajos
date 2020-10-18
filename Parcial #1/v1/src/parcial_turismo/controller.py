import tkinter as tk

from parcial_turismo.model import Model
from parcial_turismo.view import View


class Controller:
    # Inits
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()

        self.work_cant = 1
        self.work_subtotal = 0.0
        self.work_descuento = 0.0
        self.work_es_jubilado = False
        self.work_abono = 0

        self.view = View(self.root, self)

    def start(self):
        self.root.title("Parcial & Proyecto #1")
        self.root.resizable(False, False)
        self.root.mainloop()

    # Controller actions
    def update_work_vars(self):
        self.work_subtotal = self.model.zona_act.precio * float(self.work_cant)

        descuento = 0
        if self.work_es_jubilado:
            descuento += 0.10

        if self.work_cant >= 3:
            descuento += 0.15

        if self.work_subtotal > 2000:
            descuento += 0.05

        self.work_descuento = self.work_subtotal * descuento

    # Model setters
    def set_regionact_by_nombre(self, nombre):
        self.model.set_regionact_by_nombre(nombre)

    def set_objact(self, obj):
        tipo = self.model.get_tipo_obj(obj)
        if tipo == "region":
            self.set_regionact(obj)
            self.set_zonaact(None)
        elif tipo == "zona":
            self.set_zonaact(obj)

    def set_regionact(self, region):
        self.model.region_act = region

    def set_zonaact(self, zona):
        self.model.zona_act = zona

    def set_cliente_act(self, e):
        self.model.set_cliente_act(e, self.work_es_jubilado)

    def add_reserva(self):
        self.model.add_reserva(self.work_cant, self.work_subtotal, self.work_descuento)
        self.work_cant = 1
        self.work_subtotal = 0.0
        self.work_descuento = 0.0
        self.work_abono = 0
        self.work_es_jubilado = False

    def remove_reserva(self, index):
        self.model.reserva_list.pop(index)

    def clear_reservas(self):
        self.model.reserva_list.clear()
        self.model.cliente_act = None

    # Model getters
    def get_tipo_obj(self, obj):
        return self.model.get_tipo_obj(obj)
