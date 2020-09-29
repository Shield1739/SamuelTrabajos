from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

# Global var

lista_estudiantes = []


# classes

class Estudiante:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = []

    def add_nota(self, nota):
        self.notas.append(nota)

    def get_promedio(self):
        if len(self.notas) <= 0:
            return 0

        promedio = 0
        for i in self.notas:
            promedio += i

        return promedio / len(self.notas)


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tarea Grupal #4 - Programa 1")
        self.geometry("500x500")
        self.resizable(False, False)

        self.main_frame = LabelFrame()
        self.sub_frame = LabelFrame()

        self.menu_strings = [
            "Agregar estudiante", "Buscar estudiante", "Modificar Nota",
            "Listar estudiantes por nombre", "Listar estudiantes por notas",
            "Mostrar media de las notas", "Borrar estudiante"]
        self.radioVar = IntVar()

        self.entry_1 = Entry()
        self.entry_2 = Entry()

        self.table = ttk.Treeview()
        self.table_notas = ttk.Treeview()

    # frames
    def create_mainframe(self):
        # , borderwidth=0, highlightthickness=0
        self.sub_frame.destroy()
        self.main_frame = LabelFrame(self, padx=10, pady=10)
        self.main_frame.pack(padx=10, pady=75)

    def create_subframe(self):
        self.main_frame.destroy()
        self.sub_frame = LabelFrame(self, padx=10, pady=10)
        self.sub_frame.pack(padx=10, pady=75)

    # Main win
    def show_main_window(self):
        self.create_mainframe()
        self.radioVar.set(0)

        Label(self.main_frame, text="Que desea elegir?").grid(row=0, column=0, sticky=W)

        for i in range(len(self.menu_strings)):
            radio_button = Radiobutton(self.main_frame, text=self.menu_strings[i], value=i + 1,
                                       variable=self.radioVar, command=self.main_window_selec)
            radio_button.grid(row=i + 1, column=0, sticky=W)

    def main_window_selec(self):
        i = self.radioVar.get()

        if i == 1:
            self.show_add_estudiante_window()
        elif i == 2:
            self.show_search_estudiante_window()
        elif i == 3:
            self.show_editar_notas_window()
        elif i == 4:
            self.show_sort_by_estudiante_window()
        elif i == 5:
            self.show_sort_by_notas_window()
        elif i == 6:
            self.show_promedio_window()
        elif i == 7:
            self.show_borrar_estudiante_window()

    # sub win
    def show_sub_window(self, title):
        back_button = Button(self.sub_frame, text="ATRAS", command=self.show_main_window)
        back_button.grid(row=0, column=0)

        Label(self.sub_frame, text=title).grid(row=0, column=1)

    # show wins
    def show_add_estudiante_window(self):
        self.create_subframe()
        self.show_sub_window("Agregar estudiante:")

        Label(self.sub_frame, text="Nombre: ").grid(row=1, column=1, sticky=W)
        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=1, column=2, sticky=W)
        Label(self.sub_frame, text="Apellido: ").grid(row=2, column=1, sticky=W)
        self.entry_2 = Entry(self.sub_frame)
        self.entry_2.grid(row=2, column=2, sticky=W)

        Button(self.sub_frame, text="AGREGAR",
               command=lambda: add_estudiante(self.entry_1.get(), self.entry_2.get())).grid(row=3, column=3)

    def show_search_estudiante_window(self):
        self.create_subframe()
        self.show_sub_window("Buscar estudiante:")

        Label(self.sub_frame, text="Nombre:").grid(row=1, column=1, sticky=W)
        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=1, column=2, sticky=W)

        Button(self.sub_frame, text="BUSCAR",
               command=lambda: search_estudiante(self.entry_1.get())).grid(row=1, column=3)

        self.crear_estudiante_table(["Nombre", "Apellido"])
        self.fill_estudiante_table(lista_estudiantes)
        self.table.grid(row=4, column=1, columnspan=4)

    def show_editar_notas_window(self):
        self.create_subframe()
        self.show_sub_window("Modificar Notas")

        Label(self.sub_frame, text="Estudiantes:").grid(row=1, column=1, sticky=W)
        Label(self.sub_frame, text="Notas:").grid(row=1, column=2, sticky=W)

        self.crear_estudiante_table(["Nombre", "Apellido"])
        self.fill_estudiante_table(lista_estudiantes)
        self.table.grid(row=2, column=1)
        self.table.bind('<ButtonRelease-1>', self.on_student_ttk_click)

        self.table_notas = ttk.Treeview(self.sub_frame, columns="Notas", show='headings')
        self.table_notas.column("Notas", minwidth=0, width=100, stretch=NO)
        self.table_notas.heading("Notas", text="Notas")
        self.table_notas.grid(row=2, column=2, columnspan=4)

        Button(self.sub_frame, text="BORRAR",
               command=lambda: borrar_nota()).grid(row=3, column=2)
        Button(self.sub_frame, text="AGREGAR",
               command=lambda: add_nota(self.entry_1.get())).grid(row=4, column=2)

        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=4, column=1, sticky=E)

    def show_sort_by_estudiante_window(self):
        self.create_subframe()
        self.show_sub_window("Listado de estudiantes por nombre:")

        self.crear_estudiante_table(["Nombre", "Apellido"])
        self.table.grid(row=1, column=1)

        nombres = []
        for i in lista_estudiantes:
            nombres.append(i.nombre)

        index_list = sorted(range(len(nombres)), key=lambda k:  nombres[k])

        for i in range(len(lista_estudiantes)):
            nombres[i] = lista_estudiantes[index_list[i]]

        self.fill_estudiante_table(nombres)

    def show_sort_by_notas_window(self):
        self.create_subframe()
        self.show_sub_window("Listado de estudiantes por nombre:")

        self.crear_estudiante_table(["Nombre", "Apellido", "Promedio"])
        self.table.grid(row=2, column=1, columnspan=4)

        notas = []
        for i in lista_estudiantes:
            notas.append(i.get_promedio())

        index_list = sorted(range(len(notas)), key=lambda k: notas[k])
        index_list.reverse()

        for i in range(len(lista_estudiantes)):
            notas[i] = lista_estudiantes[index_list[i]]

        self.table.delete(*self.table.get_children())
        for i in notas:
            self.table.insert('', 'end', text=i, values=(i.nombre, i.apellido, int(i.get_promedio())))

    def show_promedio_window(self):
        self.create_subframe()

        self.show_sub_window("Promedio de notas:")
        Label(self.sub_frame, text="Media:").grid(row=1, column=1, sticky=W)

        media = 0
        for i in lista_estudiantes:
            media += i.get_promedio()
        media /= len(lista_estudiantes)

        Label(self.sub_frame, text=int(media)).grid(row=1, column=1, columnspan=1)

        self.crear_estudiante_table(["Nombre", "Apellido", "Promedio"])
        self.table.grid(row=2, column=1, columnspan=4)

        self.table.delete(*self.table.get_children())
        for i in lista_estudiantes:
            self.table.insert('', 'end', text=i, values=(i.nombre, i.apellido, int(i.get_promedio())))

    def show_borrar_estudiante_window(self):
        self.create_subframe()

        self.show_sub_window("Borrar estudiantes:")

        self.crear_estudiante_table(["Nombre", "Apellido"])
        self.fill_estudiante_table(lista_estudiantes)
        self.table.grid(row=1, column=1)

        Button(self.sub_frame, text="BORRAR",
               command=lambda: self.borrar_estudiante()).grid(row=0, column=2, sticky=E)

    # tables & acciones
    def crear_estudiante_table(self, columns):
        self.table = ttk.Treeview(self.sub_frame, columns=columns, show='headings')
        for i in columns:
            self.table.heading(i, text=i)
            self.table.column(i, minwidth=0, width=100, stretch=NO)

    def fill_estudiante_table(self, lista):
        self.table.delete(*self.table.get_children())
        for i in range(len(lista)):
            self.table.insert('', 'end', text=i, values=(lista[i].nombre, lista[i].apellido))

    def on_student_ttk_click(self, event):
        try:
            i = int(self.table.item(self.table.focus(), "text"))
        except ValueError:
            return
        self.fill_notas_table(i)

    def fill_notas_table(self, i):
        self.table_notas.delete(*self.table_notas.get_children())
        notas = lista_estudiantes[i].notas
        for j in range(len(notas)):
            self.table_notas.insert('', 'end', text=j, values=notas[j])

    def borrar_estudiante(self):
        try:
            i = int(self.table.item(self.table.focus(), "text"))
        except ValueError:
            return
        lista_estudiantes.pop(i)

        self.fill_estudiante_table(lista_estudiantes)


# methods
def show_errorbox(msg):
    messagebox.showerror("error", msg)


def show_warningbox(msg):
    messagebox.showwarning("warning", msg)


def add_estudiante(nombre, apellido):
    if nombre == "" or apellido == "":
        show_warningbox("Los campos no pueden estar vacios")
        return
    if len(lista_estudiantes) >= 10:
        show_errorbox("No pueden haber mas de 10 estudiantes")
        return

    app.entry_1.delete(0, 'end')
    app.entry_2.delete(0, 'end')
    lista_estudiantes.append(Estudiante(nombre.lower(), apellido.lower()))


def search_estudiante(nombre):
    if nombre == "":
        show_warningbox("El campo no pueden estar vacio")
        return

    nombre = nombre.lower()
    nombre = nombre.split()
    lista = []

    for i in lista_estudiantes:
        valid = False
        for j in nombre:
            if re.match(j, i.nombre) or re.match(j, i.apellido):
                valid = True
        if valid:
            lista.append(i)

    if len(lista) > 0:
        app.fill_estudiante_table(lista)
    else:
        show_warningbox("No se encontro ese nombre en el sistema")


def add_nota(nota):
    try:
        i = int(app.table.item(app.table.focus(), "text"))
    except ValueError:
        show_warningbox("Seleccione un estudiante")
        return

    try:
        nota = int(nota)
    except ValueError:
        app.entry_1.delete(0, 'end')
        show_errorbox("La nota tiene que ser un numero")
        return

    if nota < 0 or nota > 100:
        app.entry_1.delete(0, 'end')
        show_warningbox("La nota tiene que estar entre 0-100")
        return

    app.entry_1.delete(0, 'end')
    lista_estudiantes[i].add_nota(nota)
    app.fill_notas_table(i)


def borrar_nota():
    try:
        i = int(app.table.item(app.table.focus(), "text"))
        j = int(app.table_notas.item(app.table_notas.focus(), "text"))
    except ValueError:
        show_warningbox("Seleccione un estudiante y la nota a eliminar")
        return

    lista_estudiantes[i].notas.pop(j)
    app.fill_notas_table(i)


# TODO REMOVE BEFORE RELEASE
# Lista precargada para probar
lista_estudiantes.append(Estudiante("miguel", "juls"))
lista_estudiantes[0].add_nota(70)
lista_estudiantes[0].add_nota(50)

lista_estudiantes.append(Estudiante("juan", "kiuil"))
lista_estudiantes[1].add_nota(20)
lista_estudiantes[1].add_nota(90)
lista_estudiantes[1].add_nota(50)

lista_estudiantes.append(Estudiante("angel", "kiuil"))
lista_estudiantes[2].add_nota(80)
lista_estudiantes[2].add_nota(90)
lista_estudiantes[2].add_nota(40)

# Main
app = App()
app.show_main_window()
app.mainloop()
