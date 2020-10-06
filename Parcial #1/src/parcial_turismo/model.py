class Region:
    def __init__(self, tipo, nombre, desc, zonas):
        self.tipo = tipo
        self.nombre = nombre
        self.desc = desc
        self.zonas = zonas

    def get_tipo_nombre(self):
        if self.tipo == 1:
            return "Provincia"
        else:
            return "Comarca"


class Zona:
    def __init__(self, nombre, precio, desc, extras):
        self.nombre = nombre
        self.precio = precio
        self.desc = desc
        self.extras = extras


class Reserva:
    def __init__(self, nombre, edad, nacionalidad, sexo, cedula, telefono, cnt, abono):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo
        self.cedula = cedula
        self.telefono = telefono
        self.cnt = cnt
        self.abono = abono
