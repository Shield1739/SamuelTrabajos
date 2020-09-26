from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re

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

        promedio /= len(self.notas)
        return promedio


lista_estudiantes.append(Estudiante("Miguel", "Juls"))
lista_estudiantes[0].add_nota(70)
lista_estudiantes[0].add_nota(50)

lista_estudiantes.append(Estudiante("Juan", "Kiuil"))
lista_estudiantes[1].add_nota(20)
lista_estudiantes[1].add_nota(10)
lista_estudiantes[1].add_nota(50)

lista_estudiantes.append(Estudiante("Angel", "Kiuil"))
lista_estudiantes[2].add_nota(80)
lista_estudiantes[2].add_nota(10)
lista_estudiantes[2].add_nota(40)
# global func


def show_errorbox(msg):
    messagebox.showerror("error", msg)


def show_warningbox(msg):
    messagebox.showwarning("warning", msg)


def add_estudiante(nombre, apellido):
    global lista_estudiantes

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
        show_warningbox("El campo no pueden estar vacios")
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
        app.add_student_table(lista)
    else:
        show_warningbox("No se encuentra")


def add_notas(nota):
    try:
        i = int(app.table.item(app.table.focus(), "text"))
        nota = int(nota)
    except ValueError:
        app.entry_1.delete(0, 'end')
        return

    if nota < 0 or nota > 100:
        show_warningbox("la nota tiene que estar entre 0-100")
        app.entry_1.delete(0, 'end')
        return

    lista_estudiantes[i].add_nota(nota)
    app.entry_1.delete(0, 'end')
    app.add_notas_table(i)


def borrar_nota():
    try:
        i = int(app.table.item(app.table.focus(), "text"))
        j = int(app.table_notas.item(app.table_notas.focus(), "text"))
    except ValueError:
        return

    lista_estudiantes[i].notas.pop(j)
    app.add_notas_table(i)
# tk #


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tarea Grupal #4 - Programa 1")
        self.geometry("500x500")
        self.resizable(False, False)

        self.main_frame = LabelFrame()
        self.sub_frame = LabelFrame()

        self.radioValue = IntVar()

        self.entry_1 = Entry()
        self.entry_2 = Entry()

        self.table = ttk.Treeview()
        self.table_notas = ttk.Treeview()

    # utility
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
    def main_window(self):
        self.create_mainframe()
        self.radioValue.set(0)

        Label(self.main_frame, text="Que desea elegir?").grid(row=0, column=0, sticky=W)

        rad1 = Radiobutton(self.main_frame, text="Agregar estudiante", value=1, variable=self.radioValue,
                           command=self.add_window)
        rad1.grid(row=1, column=0, sticky=W)
        rad2 = Radiobutton(self.main_frame, text="Buscar estudiante", value=2, variable=self.radioValue,
                           command=self.search_window)
        rad2.grid(row=2, column=0, sticky=W)
        rad3 = Radiobutton(self.main_frame, text="Modificar Nota", value=3, variable=self.radioValue,
                           command=self.notas_window)
        rad3.grid(row=3, column=0, sticky=W)
        rad4 = Radiobutton(self.main_frame, text="Listar estudiantes por nombre", value=4, variable=self.radioValue,
                           command=self.sort_by_estudiante)
        rad4.grid(row=4, column=0, sticky=W)
        rad5 = Radiobutton(self.main_frame, text="Listar estudiantes por notas", value=5, variable=self.radioValue,
                           command=self.sort_by_notas)
        rad5.grid(row=5, column=0, sticky=W)
        rad6 = Radiobutton(self.main_frame, text="Mostrar media de las notas", value=6, variable=self.radioValue,
                           command=self.show_media)
        rad6.grid(row=6, column=0, sticky=W)
        rad7 = Radiobutton(self.main_frame, text="Borrar estudiante", value=7, variable=self.radioValue,
                           command=self.borrar_window)
        rad7.grid(row=7, column=0, sticky=W)

    # sub window
    def sub_window(self, title):
        back_button = Button(self.sub_frame, text="ATRAS", command=self.main_window)
        back_button.grid(row=0, column=0)

        Label(self.sub_frame, text=title).grid(row=0, column=1)

    def add_window(self):
        self.create_subframe()

        self.sub_window("Añadir estudiante:")

        Label(self.sub_frame, text="Nombre: ").grid(row=1, column=1, sticky=W)
        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=1, column=2, sticky=W)
        Label(self.sub_frame, text="Apellido: ").grid(row=2, column=1, sticky=W)
        self.entry_2 = Entry(self.sub_frame)
        self.entry_2.grid(row=2, column=2, sticky=W)

        add_estudiante_button = Button(self.sub_frame, text="AGREGAR",
                                       command=lambda: add_estudiante(self.entry_1.get(), self.entry_2.get()))
        add_estudiante_button.grid(row=3, column=3)

    def search_window(self):
        self.create_subframe()

        self.sub_window("Buscar estudiante:")

        Label(self.sub_frame, text="Nombre:").grid(row=1, column=1, sticky=W)
        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=1, column=2, sticky=W)

        search_estudiante_button = Button(self.sub_frame, text="BUSCAR",
                                          command=lambda: search_estudiante(self.entry_1.get()))
        search_estudiante_button.grid(row=1, column=3)

        self.crear_student_table()
        self.add_student_table(lista_estudiantes)
        self.table.grid(row=4, column=1, columnspan=4)

    def notas_window(self):
        self.create_subframe()

        self.sub_window("Modificar Notas")

        Label(self.sub_frame, text="Estudiantes:").grid(row=1, column=1, sticky=W)
        Label(self.sub_frame, text="Notas:").grid(row=1, column=2, sticky=W)

        self.crear_student_table()
        self.add_student_table(lista_estudiantes)
        self.table.grid(row=2, column=1)
        self.table.bind('<ButtonRelease-1>', self.on_student_ttk_click)

        self.table_notas = ttk.Treeview(self.sub_frame, columns="Notas", show='headings')
        self.table_notas.column("Notas", minwidth=0, width=100, stretch=NO)
        self.table_notas.heading("Notas", text="Notas")
        # table_notas.bind('<ButtonRelease-1>', self.on_ttk_click)
        self.table_notas.grid(row=2, column=2, columnspan=4)

        borrar_nota_button = Button(self.sub_frame, text="BORRAR",
                                    command=lambda: borrar_nota())
        borrar_nota_button.grid(row=3, column=2)
        add_nota_button = Button(self.sub_frame, text="AGREGAR",
                                 command=lambda: add_notas(self.entry_1.get()))
        add_nota_button.grid(row=4, column=2)
        self.entry_1 = Entry(self.sub_frame)
        self.entry_1.grid(row=4, column=1, sticky=E)

    def crear_student_table(self):
        self.table = ttk.Treeview(self.sub_frame, columns=("Nombre", "Apellido"), show='headings')
        self.table.column("Nombre", minwidth=0, width=100, stretch=NO)
        self.table.heading("Nombre", text="Nombre")
        self.table.column("Apellido", minwidth=0, width=100, stretch=NO)
        self.table.heading("Apellido", text="Apellido")

    def add_student_table(self, lista):
        self.table.delete(*self.table.get_children())
        for i in range(len(lista)):
            self.table.insert('', 'end', text=i, values=(lista[i].nombre, lista[i].apellido))

    def on_student_ttk_click(self, event):
        try:
            i = int(self.table.item(self.table.focus(), "text"))
        except ValueError:
            return
        self.add_notas_table(i)

    def add_notas_table(self, i):
        self.table_notas.delete(*self.table_notas.get_children())
        notas = lista_estudiantes[i].notas
        for j in range(len(notas)):
            self.table_notas.insert('', 'end', text=j, values=notas[j])

    def sort_by_estudiante(self):
        self.create_subframe()

        self.sub_window("Listado de estudiantes por nombre:")
        self.crear_student_table()
        self.table.grid(row=1, column=1)

        nombres = []
        for i in lista_estudiantes:
            nombres.append(i.nombre)

        index_list = sorted(range(len(nombres)), key=lambda k:  nombres[k])

        for i in range(len(lista_estudiantes)):
            nombres[i] = lista_estudiantes[index_list[i]]

        self.add_student_table(nombres)

    def sort_by_notas(self):
        self.create_subframe()

        self.sub_window("Listado de estudiantes por nombre:")

        self.table = ttk.Treeview(self.sub_frame, columns=("Nombre", "Apellido", "Promedio"), show='headings')
        self.table.column("Nombre", minwidth=0, width=100, stretch=NO)
        self.table.heading("Nombre", text="Nombre")
        self.table.column("Apellido", minwidth=0, width=100, stretch=NO)
        self.table.heading("Apellido", text="Apellido")
        self.table.column("Promedio", minwidth=0, width=100, stretch=NO)
        self.table.heading("Promedio", text="Promedio")
        self.table.grid(row=2, column=1, columnspan=4)

        notas = []
        for i in lista_estudiantes:
            notas.append(i.get_promedio())

        index_list = sorted(range(len(notas)), key=lambda k: notas[k])

        for i in range(len(lista_estudiantes)):
            notas[i] = lista_estudiantes[index_list[i]]

        self.table.delete(*self.table.get_children())
        for i in lista_estudiantes:
            self.table.insert('', 'end', text=i, values=(i.nombre, i.apellido, int(i.get_promedio())))

    def show_media(self):
        self.create_subframe()

        self.sub_window("Promedio de notas:")
        Label(self.sub_frame, text="Media:").grid(row=1, column=1, sticky=W)

        media = 0
        for i in lista_estudiantes:
            media += i.get_promedio()
        media /= len(lista_estudiantes)

        Label(self.sub_frame, text=int(media)).grid(row=1, column=1, columnspan=1)

        self.table = ttk.Treeview(self.sub_frame, columns=("Nombre", "Apellido", "Promedio"), show='headings')
        self.table.column("Nombre", minwidth=0, width=100, stretch=NO)
        self.table.heading("Nombre", text="Nombre")
        self.table.column("Apellido", minwidth=0, width=100, stretch=NO)
        self.table.heading("Apellido", text="Apellido")
        self.table.column("Promedio", minwidth=0, width=100, stretch=NO)
        self.table.heading("Promedio", text="Promedio")
        self.table.grid(row=2, column=1, columnspan=4)

        self.table.delete(*self.table.get_children())
        for i in lista_estudiantes:
            self.table.insert('', 'end', text=i, values=(i.nombre, i.apellido, int(i.get_promedio())))

    def borrar_window(self):
        self.create_subframe()

        self.sub_window("Borrar estudiantes:")

        self.crear_student_table()
        self.add_student_table(lista_estudiantes)
        self.table.grid(row=1, column=1)

        borrar_estudiante_button = Button(self.sub_frame, text="BORRAR",
                                          command=lambda: self.borrar_estudiante())
        borrar_estudiante_button.grid(row=0, column=2, sticky=E)

    def borrar_estudiante(self):
        try:
            i = int(self.table.item(self.table.focus(), "text"))
        except ValueError:
            return
        lista_estudiantes.pop(i)

        self.add_student_table(lista_estudiantes)


app = App()
app.main_window()
app.mainloop()
