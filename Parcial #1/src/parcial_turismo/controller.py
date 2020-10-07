import tkinter as tk

from parcial_turismo.model import Model
from parcial_turismo.view import View


class Controller:
    # Inits
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()

        self.cant_var = tk.StringVar()
        self.cant_var.set("1")
        self.abono_var = tk.StringVar()
        self.abono_var.set(0)
        self.es_jubilado = tk.BooleanVar()

        self.subtotal = 0.0
        self.descuento = 0.0

        self.view = View(self.root, self)

    def start(self):
        self.root.title("Parcial & Proyecto #1")
        self.root.resizable(False, False)
        self.root.mainloop()

    # Controller actions
    def update_totales(self):
        self.subtotal = self.model.zona_act.precio * float(self.cant_var.get())

        descuento = 0
        if self.es_jubilado.get():
            descuento += 0.10

        if float(self.cant_var.get()) >= 3:
            descuento += 0.15

        if self.subtotal > 2000:
            descuento += 0.05

        self.descuento = self.subtotal * descuento

    # Model setters
    def set_regionact_by_nombre(self, nombre):
        self.model.set_regionact_by_nombre(nombre)

    def set_regionact(self, region):
        self.model.region_act = region

    def set_zonaact(self, zona):
        self.model.zona_act = zona

    def clear_reservas(self):
        self.model.reserva_list.clear()

    # Model getters
    def get_tipo_obj(self, obj):
        return self.model.get_tipo_obj(obj)
