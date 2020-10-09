import parcial_turismo as pt
from parcial_turismo.data import Region, Zona, Cliente, Reserva


class Model:
    def __init__(self):
        self.regiones = pt.get_regiones_list()
        self.region_act = None  # Region(0, "", "", "")
        self.zona_act = None  # Zona(0, "", "", "")
        self.cliente_act = None  # Cliente("Javier", "8-888-88", "60", "F", 'Panama', "999-9911", True)
        self.reserva_list = []

    def get_tipo_obj(self, obj):
        if isinstance(obj, Region):
            return "region"
        elif isinstance(obj, Zona):
            return "zona"
        else:
            # ERROR
            return "none"

    def set_cliente_act(self, e, j):
        self.cliente_act = Cliente(*e, j)

    def add_reserva(self, cant, subtotal, descuento):
        self.reserva_list.append(Reserva(self.region_act.nombre, self.region_act.get_tipo_nombre(), self.zona_act, cant,
                                         subtotal, descuento))
        self.region_act = None
        self.zona_act = None

    def set_regionact_by_nombre(self, nombre):
        if nombre == "":
            return None

        for i in self.regiones:
            if i.nombre.lower() == nombre.lower():
                self.region_act = i
