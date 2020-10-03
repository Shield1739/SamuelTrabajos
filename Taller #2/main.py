from random import randint


# Classes

class Cine:
    def __init__(self, pelicula, hora):
        self.pelicula = pelicula
        self.hora = hora


class Pelicula:
    def __init__(self, titulo, duracion, edad, director):
        self.titulo = titulo
        self.duracion = duracion
        self.edad = edad
        self.director = director


class Espectador:
    def __init__(self, nombre, dinero):
        self.nombre = nombre
        self.dinero = dinero


# Funciones

def checkint():
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Ingrese solo numeros enteros")
            continue

        return num


def checkrange(minnum, maxnum):
    while True:
        num = checkint()

        if minnum <= num <= maxnum:
            return num

        print("Rango invalido")


def checkformatoasiento():
    while True:
        cod = input().lower()
        codlist = list(cod)

        try:
            if len(codlist) != 2:
                print("FORMATO INCORRECTO! (s)")
                continue

            if not 0 < int(codlist[0]) < 9:
                print("FORMATO INCORRECTO! (c1N)")
                continue

            if not 96 < ord(codlist[1]) < 106:
                print("FORMATO INCORRECTO! (c2)")
                continue
        except ValueError:
            print("FORMATO INCORRECTO! (c1L)")

        return cod


def format_to_coords(cod):
    cod = list(cod)
    return [(int(cod[0]) * -1) + 8, (ord(cod[1]) - 97)]


def fill_sala():
    global asientos_ocupados
    for i in range(randint(20, 50)):
        x = randint(0, 7)
        y = randint(0, 8)
        if sala[x][y] == 0:
            sala[x][y] = 1
            asientos_ocupados += 1


def print_sala():
    row = 8
    col = 65
    print(f'\033[32mLIBRE \033[31m OCUPADO \033[00m Libres: {72 - asientos_ocupados}')
    for i in sala:
        for j in i:
            if j == 0:
                print("\033[32m", end="")
            else:
                print("\033[31m", end="")
            print(f'{row}{chr(col)}', end=" ")
            col += 1
        print()
        col = 65
        row -= 1
    print("\033[00m")


def elegir_asientos():
    global subtotal
    global asientos_ocupados
    while True:
        print("Ingrese el codigo del asiento que desea elegir:")
        print_sala()
        asiento = checkformatoasiento()
        asiento_coords = format_to_coords(asiento)

        if sala[asiento_coords[0]][asiento_coords[1]] == 0:
            print("Ingrese la edad:")
            edad = checkrange(1, 120)

            if edad < peliculaselec.pelicula.edad:
                print("Pelicula no es aptar par verla")
            else:
                sala[asiento_coords[0]][asiento_coords[1]] = 1
                asientos_ocupados += 1

                asientolist.append(asiento.upper())
                if edad < 13:
                    subtotal += 3.50
                elif 13 <= edad <= 59:
                    subtotal += 6.25
                else:
                    subtotal += 2.25

        else:
            print("Asiento ocupado")

        print("Si desea salir presione 0. Si desea seleccionar mas asiento presione cualquier otro numero")
        selec = checkint()

        if selec == 0:
            break


def confirmar():
    if subtotal == 0:
        print("No ha elegido ningun asiento.")
        return

    print("Ingrese su nombre:")
    nombre = input()
    print("Ingrese la cantidad de dinero que tiene:")
    dinero = checkint()

    cliente = Espectador(nombre, dinero)

    if cliente.dinero <= 0:
        # TODO RANGE CHECK
        print("pobre")
        return

    descuento = 1
    total = subtotal

    if subtotal > 30:
        descuento -= 0.1
    elif 25 <= subtotal <= 30:
        descuento -= 0.05

    if peliculaselec.hora > 2100:
        descuento -= 0.15

    total *= descuento

    if cliente.dinero < total:
        print("No tiene suficiente dinero")
        print(f'Usted tiene {cliente.dinero} y el total es {total}')
        return

    print(f'Nombre cliente: {cliente.nombre}')
    print(f'Cantidad de dinero: {cliente.dinero}\n')

    print(f'Titulo pelicula elegida: {peliculaselec.pelicula.titulo}')
    print(f'Total tiquetes: {len(asientolist)}')
    print(f'Codigo asientos: {asientolist}\n')

    print(f'Sub-Total: {subtotal}')
    print(f'Total: {total}')


def print_menu():
    print("Seleccione una opcion del menu:")
    print("1. Reservar")
    print("2. Confirmar Reserva")
    print("3. Cancelar Reserva")


# Fills

lista_peliculas = [Pelicula("3 From Hell", 120, 18, "Rob Zombie"),
                   Pelicula("Kimi no Na wa", 107, 1, "Makoto Shinkai")]

lista_cine = [Cine(lista_peliculas[0], 1800),
              Cine(lista_peliculas[1], 1700)]

sala = [[0 for i in range(9)] for j in range(8)]
asientos_ocupados = 0


# Main

fill_sala()
sala_backup = sala
asientos_ocupados_backup = asientos_ocupados

print_menu()
selec = checkint()

asientolist = []
subtotal = 0

if selec == 1:
    # Reservar

    print("Seleccione una pelicula:\n")
    print("#  %-20s Hora" % "Titulo")
    for i in range(len(lista_cine)):
        c = lista_cine[i]
        print('%d. %-20s %s' % (i+1, c.pelicula.titulo, c.hora))
    peliculaselec = lista_cine[checkrange(1, 2) - 1]

    elegir_asientos()

    if subtotal > 0:
        print(f'Sub-Total: ${subtotal}')
        print(f'Numero de asientos: {len(asientolist)}')
        print(f'Codigo de asientos: {asientolist}')

elif selec == 2:
    # Confirmar

    confirmar()

elif selec == 3:
    # Cancelar

    print("Seleccione: ")
    print("1. Agregar mas asientos")
    print("2. Cancelar reservacion")

    selec = checkrange(1, 2)

    if selec == 1:
        elegir_asientos()
    else:
        sala = sala_backup
        asientos_ocupados = asientos_ocupados_backup

        asientolist = []
        subtotal = 0

    print()
else:
    # Default
    print("Seleccion Invalida!")
