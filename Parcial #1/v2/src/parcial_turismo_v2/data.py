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


class Cliente:
    def __init__(self, nombre, cedula, edad, sexo,  nacionalidad, telefono, jubilado):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        self.telefono = telefono
        self.jubilado = jubilado

    def get_attr_list(self):
        return [self.nombre, self.cedula, self.edad, self.sexo, self.nacionalidad, self.telefono]


class Reserva:
    def __init__(self, nombre_region, tipo_region, zona, personas, subtotal, descuento):
        self.nombre_region = nombre_region
        self.tipo_region = tipo_region
        self.zona = zona
        self.personas = personas
        self.subtotal = subtotal
        self.descuento = descuento
