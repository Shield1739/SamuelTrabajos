import parcial_turismo as pt
from parcial_turismo.data import Region, Zona, Cliente, Reserva


class Model:
    def __init__(self):
        self.regiones = pt.get_regiones_list()
        self.region_act = None  # Region(0, "", "", "")
        self.zona_act = None  # Zona(0, "", "", "")
        self.cliente_act = None  # Cliente("Javier", "18", "Panama", True, 'F', "8-888-8888", "999-0101")
        self.reserva_list = []

    def get_tipo_obj(self, obj):
        if isinstance(obj, Region):
            return "region"
        elif isinstance(obj, Zona):
            return "zona"
        else:
            # ERROR
            return "none"

    def set_regionact_by_nombre(self, nombre):
        if nombre == "":
            return None

        for i in self.regiones:
            if i.nombre.lower() == nombre.lower():
                self.region_act = i
