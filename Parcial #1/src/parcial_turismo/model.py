class Region:
    def __init__(self, tipo, nombre, desc, zonas):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__desc = desc
        self.__zonas = zonas

    def get_tipo_id(self):
        return self.__tipo

    def get_tipo_nombre(self):
        if self.__tipo == 1:
            return "Provincia"
        else:
            return "Comarca"

    def get_nombre(self):
        return self.__nombre

    def get_desc(self):
        return self.__desc

    def get_zonas(self):
        return self.__zonas


class Zona:
    def __init__(self, nombre, precio, desc, extras):
        self.__nombre = nombre
        self.__precio = precio
        self.__desc = desc
        self.__extras = extras

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_desc(self):
        return self.__desc

    def get_extras(self):
        return self.__extras
