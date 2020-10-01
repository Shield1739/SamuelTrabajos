from tkinter import *
from tkinter import messagebox
from tkinter import ttk

ingredientes_list = [
    ["Peperroni", 1],
    ["Jamon", 2],
    ["Bacon", 3],
    ["Cebolla", 1],
    ["Pimenton", 1],
    ["Hongos", 2],
    ["Tomate", 1],
    ["Aceitunas", 3],
]

size_list = [
    ["Personal", 5, "S"],
    ["Mediano", 7, "M"],
    ["Familiar", 10, "L"]
]

pizza_list = []


class Pizza:
    def __init__(self, size, ingredientes, combo, total):
        self.size = size
        self.ingredientes = ingredientes
        self.combo = combo
        self.total = total


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tarea Grupal #4 - Programa 2")
        self.geometry("600x400")
        self.resizable(False, False)

        self.main_frame = LabelFrame()
        self.sub_frame = LabelFrame()

        self.total = 0
        self.total_label = Label()
        self.subtotal = 0
        self.subtotal_label = Label()

        self.selected_size = 0

        self.radioVar = IntVar()
        self.comboVar = IntVar()

        self.checkbutton_count = 0
        self.checkbutton_var_list = []

        for _ in ingredientes_list:
            self.checkbutton_var_list.append(IntVar())

        self.table = ttk.Treeview()

    # frames
    def create_mainframe(self):
        # , borderwidth=0, highlightthickness=0
        self.sub_frame.destroy()
        self.main_frame = LabelFrame(self, padx=10, pady=0)
        self.main_frame.pack(padx=10, pady=40)

    def create_subframe(self):
        self.main_frame.destroy()
        self.sub_frame = LabelFrame(self, padx=10, pady=0)
        self.sub_frame.pack(padx=10, pady=40)

    # main win
    def show_main_window(self):
        self.create_mainframe()

        self.clean_variables()
        self.total = 0
        del pizza_list[:]

        Label(self.main_frame, text="Menu de pizza").grid(row=0, column=0)
        # Size
        Label(self.main_frame, text="Tamaño:").grid(row=1, column=0, sticky=W)
        for i in range(len(size_list)):
            k = size_list[i]
            Radiobutton(self.main_frame, text=k[0] + " $" + str(k[1]), value=i + 1, variable=self.radioVar,
                        command=lambda j=i + 1: self.selec_size(j)).grid(row=i + 2, column=0, sticky=W)

        # Combo
        Label(self.main_frame, text="Otros:").grid(row=5, column=0, sticky=W)
        Checkbutton(self.main_frame, text="Combo $5", onvalue=1, offvalue=0, variable=self.comboVar,
                    command=self.selec_combo).grid(row=6, column=0, sticky=W)

        # Ingredientes
        Label(self.main_frame, text="Ingredientes:").grid(row=1, column=1, sticky=W)
        for i in range(len(ingredientes_list)):
            k = ingredientes_list[i]
            Checkbutton(self.main_frame, text=k[0],
                        variable=self.checkbutton_var_list[i], onvalue=1, offvalue=0,
                        command=lambda j=i: self.add_ingrediente(j)).grid(row=i + 2, column=1, sticky=W)
            Label(self.main_frame, text="$" + str(k[1])).grid(row=i + 2, column=2, sticky=W)

        self.subtotal_label = Label(self.main_frame, text="SubTotal: $" + str(self.subtotal))
        self.subtotal_label.grid(row=11, column=1, sticky=W)
        Button(self.main_frame, text="Agregar", command=self.add_pizza).grid(row=11, column=2)

        # Tabla
        columnas = ["Size", "Ing", "Combo", "$"]
        self.table = ttk.Treeview(self.main_frame, columns=columnas, show='headings')
        for i in columnas:
            self.table.heading(i, text=i)
            self.table.column(i, minwidth=0, width=50, stretch=NO)
        self.table.grid(row=1, column=3, rowspan=10)

        self.total_label = Label(self.main_frame, text="Total: $" + str(self.subtotal))
        self.total_label.grid(row=11, column=3, columnspan=3)
        Button(self.main_frame, text="CHECKOUT", command=self.show_checkout_window).grid(row=11, column=3, columnspan=4, sticky=E)

    # check out win
    def show_checkout_window(self):
        if len(pizza_list) == 0:
            show_errorbox("No ha agregado ninguna pizza")
            return

        self.create_subframe()

        Button(self.sub_frame, text="ATRAS", command=self.show_main_window).grid(row=0, column=0)
        Label(self.sub_frame, text="Checkout").grid(row=0, column=1)
        Label(self.sub_frame, text="Sub-Total:").grid(row=1, column=1, sticky=E)
        Label(self.sub_frame, text="$" + str(self.total)).grid(row=1, column=2, sticky=W)

        descuento = 0
        if self.total >= 20:
            valid = False
            for i in pizza_list:
                if i.combo == "Si":
                    valid = True

            if valid:
                if self.total >= 30:
                    descuento = self.total * 0.05
                else:
                    descuento = self.total * 0.02
            else:
                show_warningbox("No tiene combos en su cuenta. No aplica descuento")
        else:
            show_warningbox("Compra menos de $20. No aplica descuento")

        Label(self.sub_frame, text="Descuento:").grid(row=2, column=1, sticky=E)
        Label(self.sub_frame, text="$" + str(descuento)).grid(row=2, column=2, sticky=W)
        Label(self.sub_frame, text="Total:").grid(row=3, column=1, sticky=E)
        Label(self.sub_frame, text="$" + str(self.total - descuento)).grid(row=3, column=2, sticky=W)

    # acciones
    def refresh_subtotal(self):
        self.subtotal_label.config(text="SubTotal: $" + str(self.subtotal))

    def selec_size(self, size):
        if self.selected_size != 0:
            self.subtotal -= size_list[self.selected_size-1][1]

        self.selected_size = self.radioVar.get()
        self.subtotal += size_list[size-1][1]

        self.refresh_subtotal()

    def selec_combo(self):
        if self.comboVar.get() == 1:
            self.subtotal += 5
        else:
            self.subtotal -= 5
        self.refresh_subtotal()

    def add_ingrediente(self, cid):
        if self.checkbutton_var_list[cid].get() == 1:
            if self.checkbutton_count >= 3:
                show_errorbox("Solo puede seleccionar 3 ingredientes")
                self.checkbutton_var_list[cid].set(0)
                return
            self.checkbutton_count += 1
            self.subtotal += ingredientes_list[cid][1]
        else:
            self.checkbutton_count -= 1
            self.subtotal -= ingredientes_list[cid][1]
        self.refresh_subtotal()

    def add_pizza(self):
        if self.selected_size == 0:
            show_warningbox("Tiene que seleccionar un tamano")
            return

        for i in self.checkbutton_var_list:
            i.set(0)

        if self.comboVar.get() == 1:
            combo = "Si"
        else:
            combo = "No"

        pizza_list.append(Pizza(size_list[self.selected_size-1][2], self.checkbutton_count, combo, self.subtotal))

        self.total += self.subtotal
        self.total_label.config(text="Total: $" + str(self.total))

        self.clean_variables()
        self.fill_pizza_table()

        self.refresh_subtotal()

    def clean_variables(self):
        self.checkbutton_count = 0
        self.selected_size = 0
        self.radioVar.set(0)
        self.comboVar.set(0)
        self.subtotal = 0

    def fill_pizza_table(self):
        self.table.delete(*self.table.get_children())
        for i in range(len(pizza_list)):
            pizza = pizza_list[i]
            self.table.insert('', 'end', text=i, values=(pizza.size, pizza.ingredientes, pizza.combo,
                                                         "$"+str(pizza.total)))


# funciones
def show_errorbox(msg):
    messagebox.showerror("error", msg)


def show_warningbox(msg):
    messagebox.showwarning("warning", msg)


app = App()
app.show_main_window()
app.mainloop()
