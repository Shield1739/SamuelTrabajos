from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CategoriaPlato:
    def __init__(self, tipo, platos):
        self.tipo = tipo
        self.platos = platos


class Plato:
    def __init__(self, nombre, desc, precio):
        self.nombre = nombre
        self.desc = desc
        self.precio = int(precio)


# Global
Menu = [
    CategoriaPlato("Platos de Entradas", [
        Plato("Plato E #1", "Lorem Ipsum", 2),
        Plato("Plato E #2", "Lorem Ipsum", 2),
        Plato("Plato E #3", "Lorem Ipsum", 4),
        Plato("Plato E #4", "Lorem Ipsum", 5)
    ]),
    CategoriaPlato("Platos Fuertes", [
        Plato("Plato F #1", "Lorem Ipsum", 6),
        Plato("Plato F #2", "Lorem Ipsum", 8),
        Plato("Plato F #3", "Lorem Ipsum", 10),
        Plato("Plato F #4", "Lorem Ipsum", 12)
    ]),
    CategoriaPlato("Bebidas", [
        Plato("Bebida #1", "Lorem Ipsum", 1),
        Plato("Bebida #2", "Lorem Ipsum", 2),
        Plato("Bebida #3", "Lorem Ipsum", 2),
        Plato("Bebida #4", "Lorem Ipsum", 3)
    ]),
    CategoriaPlato("Postres", [
        Plato("Postres #1", "Lorem Ipsum", 3),
        Plato("Postres #2", "Lorem Ipsum", 3),
        Plato("Postres #3", "Lorem Ipsum", 6),
        Plato("Postres #4", "Lorem Ipsum", 7)
    ])
]

Orden = []


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Taller #3")
        self.geometry("575x550")
        self.resizable(False, False)

        self.frame = LabelFrame()

        self.combobox = ttk.Combobox()
        self.combobox_var = StringVar()
        self.combobox_strings = []
        for i in Menu:
            self.combobox_strings.append(i.tipo)

        self.table_menu = ttk.Treeview()
        self.table_orden = ttk.Treeview()

        self.jubiladoVar = IntVar()

        self.subtotal = 0.0

        self.subtotal_label = Label()
        self.descuento_label = Label()
        self.total_label = Label()

    # frames
    def create_new_frame(self):
        self.frame.destroy()
        self.frame = LabelFrame(self, padx=10, pady=0, borderwidth=0, highlightthickness=0)
        self.frame.pack(padx=10, pady=40)

    # main win
    def show_main_window(self):
        self.create_new_frame()

        # Combobox
        Label(self.frame, text="Eliga una opcion:").grid(row=1, column=0, sticky=W)

        self.combobox = ttk.Combobox(self.frame, textvariable=self.combobox_var, width=15, values=self.combobox_strings)
        self.combobox.bind("<<ComboboxSelected>>", self.combobox_selec)
        self.combobox.grid(row=2, column=0, sticky=NW)

        Label(self.frame, text="").grid(row=0, column=1, sticky=W)

        # menu
        Label(self.frame, text="Bienvenidos al Restaurante “Maido Café”").grid(row=0, column=2, columnspan=5)
        Label(self.frame, text="Menu:").grid(row=1, column=2, sticky=W)

        self.table_menu = ttk.Treeview(self.frame, height=5, columns=["Nombre", "Descripcion", "Precio"], show='headings')
        self.table_menu.heading("#1", text="Nombre")
        self.table_menu.column("#1", minwidth=0, width=100, stretch=NO)
        self.table_menu.heading("#2", text="Descripcion")
        self.table_menu.column("#2", minwidth=0, width=250, stretch=NO)
        self.table_menu.heading("#3", text="Precio")
        self.table_menu.column("#3", minwidth=0, width=50, stretch=NO)
        self.table_menu.grid(row=2, column=2, columnspan=2, sticky=W)

        Button(self.frame, text="AGREGAR",
               command=lambda: self.add_plato()).grid(row=3, column=3, sticky=E)

        # Orden
        Label(self.frame, text="Orden Actual:").grid(row=4, column=2, sticky=W)

        self.table_orden = ttk.Treeview(self.frame, columns=["Tipo", "Nombre", "Precio"], show='headings')
        self.table_orden.heading("#1", text="Tipo")
        self.table_orden.column("#1", minwidth=0, width=105, stretch=NO)
        self.table_orden.heading("#2", text="Nombre")
        self.table_orden.column("#2", minwidth=0, width=150, stretch=NO)
        self.table_orden.heading("#3", text="Precio")
        self.table_orden.column("#3", minwidth=0, width=50, stretch=NO)
        self.table_orden.grid(row=5, column=2, rowspan=5, sticky=W)

        Button(self.frame, text="ELIMINAR",
               command=lambda: self.del_plato()).grid(row=10, column=2, sticky=E)

        # Checkout
        Label(self.frame, text="Checkout:").grid(row=5, column=3, sticky=NW)

        Checkbutton(self.frame, text="Es Jubilado?", onvalue=1, offvalue=0, variable=self.jubiladoVar,
                    command=lambda: self.refresh_labels()).grid(row=5, column=3, sticky=W)

        self.refresh_labels()

        Button(self.frame, text="PAGAR",
               command=lambda: self.pagar()).grid(row=7, column=3, sticky=W)

    def combobox_selec(self, event):
        self.fill_table(Menu[self.combobox.current()].platos)

    def fill_table(self, lista):
        self.table_menu.delete(*self.table_menu.get_children())
        for i in range(len(lista)):
            e = lista[i]
            self.table_menu.insert('', 'end', text=i, values=(e.nombre, e.desc, "$" + str(e.precio)))

    def add_plato(self):
        try:
            tipo = int(self.combobox.current())
            plato = int(self.table_menu.item(self.table_menu.focus(), "text"))
        except ValueError:
            show_warningbox("Seleccione un plato")
            return

        Orden.append([tipo, plato])
        self.update_orden()

    def del_plato(self):
        try:
            plato = int(self.table_orden.item(self.table_orden.focus(), "text"))
        except ValueError:
            show_warningbox("Seleccione un plato")
            return

        Orden.pop(plato)
        self.update_orden()

    def update_orden(self):
        self.table_orden.delete(*self.table_orden.get_children())
        self.subtotal = 0
        for i in range(len(Orden)):
            e = Menu[Orden[i][0]]
            plato = e.platos[Orden[i][1]]
            self.subtotal += plato.precio
            self.table_orden.insert('', 'end', text=i, values=(e.tipo, plato.nombre, "$" + str(plato.precio)))
        self.refresh_labels()

    # acciones
    def refresh_labels(self):
        self.subtotal_label.destroy()
        self.descuento_label.destroy()
        self.total_label.destroy()

        self.subtotal_label = Label(self.frame, text="Sub-Total: $" + str(round(self.subtotal, 2)))
        self.subtotal_label.grid(row=6, column=3, sticky=NE)

        descuento_p = 0.0
        if self.subtotal > 50:
            descuento_p = 0.1

        if self.jubiladoVar.get() == 1:
            descuento_p += 0.05

        descuento = self.subtotal * descuento_p

        self.descuento_label = Label(self.frame, text="Descuento: $" + str(round(descuento, 2)))
        self.descuento_label.grid(row=6, column=3, sticky=E)

        self.total_label = Label(self.frame, text="Total: $" + str(round(self.subtotal - descuento, 2)))
        self.total_label.grid(row=6, column=3, sticky=SE)

    def pagar(self):
        self.subtotal = 0.0
        Orden.clear()
        self.frame.destroy()
        self.create_new_frame()

        Label(self.frame, text="Gracias por comer en “Maido Café”").pack()


# funciones
def show_warningbox(msg):
    messagebox.showwarning("warning", msg)


# Main
app = App()
app.show_main_window()
app.mainloop()
