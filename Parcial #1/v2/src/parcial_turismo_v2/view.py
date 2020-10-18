import os

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext as st
from tkinter.font import Font

from PIL import ImageTk, Image

from parcial_turismo_v2 import Tipos


class BaseView:
    FONT_SMALL = "ubuntu 10"
    FONT_MEDIUM = "ubuntu 12"
    FONT_LARGE = "ubuntu 14"
    FONT_HUGE = "ubuntu 16"

    orange = '#F57C00'
    purple = '#9965f4'
    pink = '#FF0266'
    green = "#41c300"
    red = '#ef5350'

    def __init__(self, parent, controller):
        super(BaseView, self).__init__()
        self._parent = parent
        self._controller = controller
        self._variables = {}
        self._widgets = {}

    @property
    def parent(self):
        return self._parent

    @property
    def controller(self):
        return self._controller

    @property
    def variables(self):
        return self._variables

    @property
    def widgets(self):
        return self._widgets

    def create_frame(self):
        frame = ttk.Frame(self.parent)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        frame.pack(expand=tk.TRUE, fill=tk.BOTH, padx=25, pady=25)
        return frame

    # Variables & Widget managers
    def has_variable(self, name):
        return name in self.variables.keys()

    def add_variable(self, name, variable):
        if self.has_variable(name):
            raise KeyError("Variable ya existe en el view")
        self.variables[name] = variable
        return variable

    def get_variable(self, name):
        if not self.has_variable(name):
            raise KeyError("Variable no existe en el view")
        return self.variables[name]

    def remove_variable(self, name):
        if not self.has_variable(name):
            raise KeyError("Variable no existe en el view")
        self.variables.pop(name)
        return not self.has_variable(name)

    def has_widget(self, name):
        return name in self.widgets.keys()

    def add_widget(self, name, widget):
        if self.has_widget(name):
            raise KeyError("Variable ya existe en el view")
        self.widgets[name] = widget
        return widget

    def get_widget(self, name):
        if not self.has_widget(name):
            raise KeyError("Variable no existe en el view")
        return self.widgets[name]

    def remove_widget(self, name):
        if not self.has_widget(name):
            raise KeyError("Variable no existe en el view")
        self.widgets.pop(name)
        return not self.has_widget(name)


class PresentacionWindowView(BaseView):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.parent.geometry("600x600")

        self.frame = self.create_frame()

        self.show_presentacion_window()

    def show_presentacion_window(self):
        style = ttk.Style()
        style.configure('M.TLabel', font=self.FONT_MEDIUM)

        ttk.Label(self.frame, text="UNIVERSIDAD TECNOLÓGICA DE PANAMÁ").pack()
        ttk.Label(self.frame, text="FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES").pack()
        ttk.Label(self.frame, text="DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS").pack()
        ttk.Label(self.frame, text="CARRERA LICENCIATURA EN INGENIERÍA DE SOFTWARE").pack()
        ttk.Label(self.frame, text="INTRODUCCIÓN A LA TEORÍA COMPUTACIONAL").pack()

        ttk.Label(self.frame, text="PARCIAL & PROYECTO #1").pack(pady=25)

        ttk.Label(self.frame, text="INTEGRANTES:").pack(pady=5)
        ttk.Label(self.frame, text="Kevin Feng - 3-748-410").pack()
        ttk.Label(self.frame, text="Angel Iglesias - 8-958-1").pack()
        ttk.Label(self.frame, text="Sahori Raby - 8-964-644").pack()
        ttk.Label(self.frame, text="Luis Villalaz - 8-925-2287").pack()
        ttk.Label(self.frame, text="Wyming Zeng - 8-966-1043").pack()

        ttk.Label(self.frame, text="").pack(pady=10)

        ttk.Label(self.frame, text="Profesor:").pack(pady=5)
        ttk.Label(self.frame, text="Ing. Samuel Jiménez").pack()

        ttk.Label(self.frame, text="SEMESTRE II, 2020").pack(pady=25)

        widgets = self.frame.winfo_children()
        for i in widgets:
            i.configure(style='M.TLabel')

        ttk.Button(self.frame, text="EMPEZAR", command=self.create_mapa_window).pack(pady=10)

    def create_mapa_window(self):
        self.controller.create_mapa_view()


class MapaWindowView(BaseView):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.parent.geometry("900x600")

        self.frame = self.create_frame()

        self.canvas_font = Font(family='ubuntu', size=10, weight='bold')

        self.show_mapa_window()

    def show_mapa_window(self):
        ttk.Label(self.frame, text="ELIJA SU DESTINO", font=self.FONT_HUGE).pack()

        mapa = tk.Canvas(self.frame, height=400, width=800)
        self.add_widget("mapa", mapa)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img = ImageTk.PhotoImage(Image.open(str(dir_path) + '/img/panama.png'))
        mapa.image = img
        mapa.create_image(400, 200, image=img)
        mapa.pack()

        self.create_provincias_text()
        self.create_comarcas_text()

        mapa.tag_bind("t", "<Button-1>", self.on_canvas_click)

        ttk.Label(self.frame, text="MOSTAR:", font=self.FONT_MEDIUM).pack(side=tk.LEFT, pady=25)

        display_var = tk.IntVar()
        display_var.set(0)
        self.add_variable("display_var", display_var)

        ttk.Radiobutton(self.frame, text="SOLO PROVINCIAS", value=2, variable=display_var,
                        command=lambda: self.change_display_mode()).pack(side=tk.LEFT)
        ttk.Radiobutton(self.frame, text="SOLO COMARCAS", value=1, variable=display_var,
                        command=lambda: self.change_display_mode()).pack(side=tk.LEFT)
        ttk.Radiobutton(self.frame, text="AMBAS", value=0, variable=display_var,
                        command=lambda: self.change_display_mode()).pack(side=tk.LEFT)

        ttk.Button(self.frame, text="PAGAR", command=self.create_pagar_window).pack(side=tk.RIGHT)
        ttk.Button(self.frame, text="CANCELAR RESERVAS", command=self.cancelar_reservas).pack(side=tk.RIGHT)

    def create_provincias_text(self):
        mapa = self.get_widget("mapa")
        canvas_text_provincias = [mapa.create_text(70, 100, text='BOCAS\nDEL TORO'),
                                  mapa.create_text(90, 180, text='CHIRIQUÍ'),
                                  mapa.create_text(265, 230, text='VERAGUAS'),
                                  mapa.create_text(320, 270, text='HERRERA'),
                                  mapa.create_text(370, 320, text='LOS SANTOS'),
                                  mapa.create_text(360, 190, text='COCLÉ'),
                                  mapa.create_text(425, 155, text='PANAMÁ\nOESTE'),
                                  mapa.create_text(360, 125, text='COLÓN'),
                                  mapa.create_text(510, 110, text='PANAMÁ'),
                                  mapa.create_text(700, 260, text='DARIÉN')]

        for i in canvas_text_provincias:
            mapa.itemconfig(i, fill=self.orange, activefill=self.pink, tag='t', font=self.canvas_font)

    def create_comarcas_text(self):
        mapa = self.get_widget("mapa")
        canvas_text_comarcas = [mapa.create_text(195, 175, text='NGÖBE-BUGLÉ'),
                                mapa.create_text(650, 80, text='GUNA YALA'),
                                mapa.create_text(730, 200, text='EMBERÁ')]

        for i in canvas_text_comarcas:
            mapa.itemconfig(i, fill=self.orange, activefill=self.pink, tag='t', font=self.canvas_font)

    def change_display_mode(self):
        self.get_widget("mapa").delete("t")

        e = self.get_variable("display_var").get()
        if e == 2:
            self.create_provincias_text()
        elif e == 1:
            self.create_comarcas_text()
        else:
            self.create_provincias_text()
            self.create_comarcas_text()

    def on_canvas_click(self, event):
        w = event.widget
        i = w.find_closest(event.x, event.y)

        try:
            r = w.itemcget(*i, "text")
        except tk.TclError:
            return

        r = r.replace("\n", " ")

        self.controller.set_region_act_by_nombre(r)
        self.create_select_window()

    def cancelar_reservas(self):
        if len(self.controller.get_reservalist()) > 0:
            if messagebox.askyesno("Mensaje", "Esta seguro que quiere cancelar sus reservas??"):
                self.controller.clear_reservalist()
        else:
            messagebox.showwarning("Warning", "No tiene reservas activas")

    def create_select_window(self):
        self.controller.create_select_view()

    def create_pagar_window(self):
        if len(self.controller.get_reservalist()) > 0:
            self.controller.create_pagar_view()
        else:
            messagebox.showwarning("Warning", "No tiene reservas activas")


class SelectWindowView(BaseView):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.parent.geometry("900x600")

        self.frame = self.create_frame()

        self.s = ttk.Style()
        self.s.configure('M.TRadiobutton', font=self.FONT_MEDIUM)

        self.show_sub_window()

    def show_sub_window(self):
        ttk.Button(self.frame, text="\u21E6 ATRAS", command=self.handle_back_button).place(x=0, y=0)

        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Titulo
        ttk.Label(self.frame, text="ELIJA SU DESTINO", font=self.FONT_HUGE).pack(pady=0)

        if self.controller.get_obj_act(Tipos.ZONA) is None:
            region = self.controller.get_obj_act(Tipos.REGION)
            desc = region.desc

            ttk.Label(self.frame, text=region.nombre, font=self.FONT_LARGE).pack()

            frame3_titulo = "Zonas Turisticas"
            img_path = str(dir_path) + '/img/mapas/' + str(region.nombre) + '.png'
        else:
            region = self.controller.get_obj_act(Tipos.REGION)
            zona = self.controller.get_obj_act(Tipos.ZONA)
            self.controller.set_obj_act(Tipos.ZONA, zona)
            desc = zona.desc

            ttk.Label(self.frame, text=zona.nombre, font=self.FONT_LARGE).pack()

            frame3_titulo = "Incluye"
            img_path = str(dir_path) + '/img/zonas/' + str(region.nombre) + '/' + str(
                zona.nombre) + '.png'

        # # Frames
        # Imagen
        frame_foto = ttk.Frame(self.frame, width=426, height=240)
        frame_foto.pack()

        img = ImageTk.PhotoImage(Image.open(img_path))

        canvas = tk.Canvas(frame_foto, width=426, height=240)
        canvas.pack(expand=tk.YES, fill=tk.BOTH)

        canvas.image = img
        canvas.create_image(213, 120, image=img, anchor=tk.CENTER)

        # Descripcion
        frame_desc = ttk.LabelFrame(self.frame, text="Descripcion", width=350, height=230)
        frame_desc.pack_propagate(False)
        frame_desc.pack(side=tk.LEFT)

        descripcion_box = st.ScrolledText(frame_desc, font=self.FONT_SMALL, wrap=tk.WORD, borderwidth=1,
                                          highlightthickness=1)
        descripcion_box.insert(tk.INSERT, desc)
        descripcion_box.config(state=tk.DISABLED)
        descripcion_box.pack(expand=True, fill=tk.BOTH)

        # Zonas/Extras
        frame3 = ttk.LabelFrame(self.frame, text=frame3_titulo, width=350, height=230)
        frame3.pack_propagate(False)
        frame3.pack(side=tk.RIGHT)

        if self.controller.get_obj_act(Tipos.ZONA) is None:
            zonas = self.controller.get_obj_act(Tipos.REGION).zonas
            for i in zonas:
                ttk.Button(frame3, text=i.nombre, command=lambda j=i: self.select_zona(j), width=40) \
                    .pack(pady=5)
        else:
            zona = self.controller.get_obj_act(Tipos.ZONA)

            extras_frame = ttk.Frame(frame3, width=350, height=150)
            extras_frame.pack_propagate(False)
            extras_frame.pack()

            extras_box = st.ScrolledText(extras_frame, font=self.FONT_SMALL, wrap=tk.WORD, borderwidth=1,
                                         highlightthickness=1, height=100)
            extras_box.insert(tk.INSERT, zona.extras)
            extras_box.config(state=tk.DISABLED)
            extras_box.pack()

            ttk.Label(frame3, text="Precio: $" + str(zona.precio), font=self.FONT_MEDIUM).pack(side=tk.LEFT)
            ttk.Button(frame3, text="RESERVAR", command=self.create_reservar_window).pack(side=tk.RIGHT)

    def handle_back_button(self):
        if self.controller.get_obj_act(Tipos.ZONA) is None:
            self.create_mapa_window()
        else:
            self.controller.set_obj_act(Tipos.ZONA, None)
            self.create_select_window()

    def select_zona(self, zona):
        self.controller.set_obj_act(Tipos.ZONA, zona)
        self.create_select_window()

    def create_select_window(self):
        self.controller.create_select_view()

    def create_mapa_window(self):
        self.controller.create_mapa_view()

    def create_reservar_window(self):
        self.controller.create_reservar_view()


class ReservarWindowView(BaseView):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.parent.geometry("900x600")

        self.frame = self.create_frame()

        self.add_variable("subtotal_var", tk.StringVar())
        self.add_variable("descuento_var", tk.StringVar())
        self.add_variable("total_var", tk.StringVar())

        self.add_variable("jubilado_var", tk.BooleanVar())

        self.show_reservar_window()

    def show_reservar_window(self):
        ttk.Button(self.frame, text="\u21E6 ATRAS", command=self.handle_back_button).place(x=0, y=0)

        self.add_variable("cant_var", tk.StringVar())
        self.get_variable("cant_var").set("1")
        self.get_variable("cant_var").trace('w', self.check_cant)

        # Titulo
        ttk.Label(self.frame, text="CONFIRMAR RESERVA", font=self.FONT_HUGE, relief=tk.SOLID).pack()

        # # Frames
        # Destino
        frame_destino = ttk.LabelFrame(self.frame, text="Informacion Destino", width=800, height=100)
        frame_destino.grid_propagate(False)
        frame_destino.pack(pady=10)

        ttk.Label(frame_destino, text="Region:", font=self.FONT_MEDIUM).grid(row=0, column=0, sticky=tk.E)
        region = self.controller.get_obj_act(Tipos.REGION)
        region_txt = str(region.get_tipo_nombre()) + " de " + str(region.nombre)
        ttk.Label(frame_destino, text=region_txt, font=self.FONT_SMALL).grid(row=0, column=1, sticky=tk.W)

        zona = self.controller.get_obj_act(Tipos.ZONA)
        ttk.Label(frame_destino, text="Zona:", font=self.FONT_MEDIUM).grid(row=1, column=0, sticky=tk.E)
        ttk.Label(frame_destino, text=zona.nombre, font=self.FONT_SMALL).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame_destino, text="Precio:", font=self.FONT_MEDIUM).grid(row=2, column=0, sticky=tk.E)
        ttk.Label(frame_destino, text="$" + str(zona.precio), font=self.FONT_SMALL).grid(row=2, column=1, sticky=tk.W)

        # Cliente
        frame_cliente = ttk.LabelFrame(self.frame, text="Informacion Cliente", width=400, height=300)
        frame_cliente.pack_propagate(False)
        frame_cliente.grid_propagate(False)
        frame_cliente.pack(side=tk.LEFT)

        entries_strings = ["Nombre:", "Cedula:", "Edad:", "Sexo:", "Nacionalidad:", "Telefono:"]

        for i in range(len(entries_strings)):
            j = entries_strings[i]
            ttk.Label(frame_cliente, text=j, font=self.FONT_MEDIUM).grid(row=i, column=0, sticky=tk.E)
            self.add_variable(entries_strings[i], tk.StringVar())

            var = self.get_variable(entries_strings[i])
            if j == "Sexo:":
                om = ttk.OptionMenu(frame_cliente, var, *['M', 'F'])
                om.grid(row=i, column=1, sticky=tk.W)
                self.add_widget(entries_strings[i], om)

                var.trace('w', self.check_jubilado)
                continue

            entry = ttk.Entry(frame_cliente, textvariable=var)
            entry.grid(row=i, column=1, sticky=tk.W, pady=5)

            self.add_widget(entries_strings[i], entry)

            if j == "Edad:":
                entry.config(width=5)
                var.set("18")
                ttk.Label(frame_cliente, text="Jubilado:", font=self.FONT_SMALL).grid(row=i, column=1, sticky=tk.W, padx=40)

                label = ttk.Label(frame_cliente, text="No", font=self.FONT_SMALL, foreground=self.red)
                self.add_widget("jubilado_label", label)
                label.grid(row=i, column=1, sticky=tk.W, padx=95)

                var.trace('w', self.check_jubilado)

        if self.controller.get_obj_act(Tipos.CLIENTE) is not None:
            c = self.controller.get_obj_act(Tipos.CLIENTE).get_attr_list()
            for i, j in zip(entries_strings, c):
                self.get_variable(i).set(j)

                widget = self.get_widget(i)
                widget.config(state=tk.DISABLED)

        # Pago
        frame_pago = ttk.LabelFrame(self.frame, text="Informacion Pago", width=400, height=300)
        frame_pago.pack_propagate(False)
        frame_pago.grid_propagate(False)
        frame_pago.pack(side=tk.RIGHT)

        ttk.Label(frame_pago, text="Adultos:", font=self.FONT_MEDIUM).grid(row=0, column=0, sticky=tk.E, pady=5)
        ttk.Entry(frame_pago, textvariable=self.get_variable("cant_var")).grid(row=0, column=1, sticky=tk.W)

        ttk.Label(frame_pago, text="Sub-Total:", font=self.FONT_MEDIUM).grid(row=1, column=0, sticky=tk.E, pady=5)
        ttk.Entry(frame_pago, textvariable=self.get_variable("subtotal_var"), state=tk.DISABLED).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame_pago, text="Descuento:", font=self.FONT_MEDIUM).grid(row=2, column=0, sticky=tk.E, pady=5)
        ttk.Entry(frame_pago, textvariable=self.get_variable("descuento_var"), state=tk.DISABLED).grid(row=2, column=1, sticky=tk.W)

        ttk.Label(frame_pago, text="Total:", font=self.FONT_MEDIUM).grid(row=3, column=0, sticky=tk.E, pady=5)
        ttk.Entry(frame_pago, textvariable=self.get_variable("total_var"), state=tk.DISABLED).grid(row=3, column=1, sticky=tk.W)

        ttk.Button(frame_pago, text="CANCELAR", command=self.handle_cancelar_button).place(x=5, y=230)
        ttk.Button(frame_pago, text="CONFIRMAR RESERVA", command=self.check_confirmar_reserva).place(x=190, y=230)

        self.refresh_totals()

    def handle_back_button(self):
        self.create_select_window()

    def handle_cancelar_button(self):
        if messagebox.askyesno("", "Desea cancelar y volver al menu principal?"):
            self.create_mapa_window()

    def check_cant(self, *args):
        cant = self.get_variable("cant_var")
        if cant.get() == "":
            return

        try:
            e = int(cant.get())
        except ValueError:
            messagebox.showerror("Error", "Usa solamente numeros en el campo de adultos")
            cant.set(self.controller.get_var_act(Tipos.PERSONAS))
            return

        if e <= 0 or e > 10:
            messagebox.showerror("Error", "La cantidad de adultos debe ser mayor que 0 y menor que 10")
            cant.set(self.controller.get_var_act(Tipos.PERSONAS))
            return

        self.controller.set_var_act(Tipos.PERSONAS, e)
        self.refresh_totals()

    def check_jubilado(self, *args):
        edad = self.get_variable("Edad:")
        sexo = self.get_variable("Sexo:")
        if edad.get() == "":
            return

        try:
            e = int(edad.get())
        except ValueError:
            messagebox.showwarning("Warning", "La edad solo puede ser un numero")
            edad.set("18")
            return

        label = self.get_widget("jubilado_label")

        if e >= 57 and sexo.get() == "F":
            label.config(text="Si", foreground=self.green)
            self.controller.set_var_act(Tipos.JUBILADO, True)
        elif e >= 62 and sexo.get() == "M":
            label.config(text="Si", foreground=self.green)
            self.controller.set_var_act(Tipos.JUBILADO, True)
        else:
            label.config(text="No", foreground=self.red)
            self.controller.set_var_act(Tipos.JUBILADO, False)

        self.refresh_totals()

    def check_confirmar_reserva(self):
        if self.controller.get_obj_act(Tipos.CLIENTE) is None:
            for i in self.variables.values():
                if i.get() == "":
                    messagebox.showerror("Error", "Los campos de informacion del cliente no pueden estar vacios")
                    return

            if int(self.get_variable("Edad:").get()) < 18:
                messagebox.showwarning("Warning", "La edad tiene que ser mayor que 18")
                self.get_variable("Edad:").set("18")
                return

            self.controller.set_new_cliente_act(self.variables)

        self.controller.add_reserva()

        r = messagebox.askyesno("Mensaje", "Desea agregar otra reserva?")
        if r:
            self.create_mapa_window()
        else:
            self.create_pagar_window()

    def refresh_totals(self):
        self.controller.update_act_vars()

        subtotal = self.controller.get_var_act(Tipos.SUBTOTAL)
        descuento = self.controller.get_var_act(Tipos.DESCUENTO)
        self.get_variable("subtotal_var").set("$" + str(subtotal))
        self.get_variable("descuento_var").set("$" + str(descuento))
        self.get_variable("total_var").set("$" + str(subtotal - descuento))

    def create_mapa_window(self):
        self.controller.create_mapa_view()

    def create_select_window(self):
        self.controller.create_select_view()

    def create_pagar_window(self):
        self.controller.create_pagar_view()


class PagarWindowView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.parent.geometry("900x600")

        self.frame = self.create_frame()

        self.show_pagar_window()

    def show_pagar_window(self):
        ttk.Button(self.frame, text="\u21E6 ATRAS", command=self.handle_back_button).place(x=0, y=0)

        ttk.Label(self.frame, text="PAGAR", font=self.FONT_HUGE, relief=tk.SOLID).pack()

        # # Frames
        # Reservas
        frame_reservas = ttk.LabelFrame(self.frame, text="Reservas", width=475, height=475)
        frame_reservas.config(relief=tk.SOLID, borderwidth=2)
        frame_reservas.pack_propagate(False)
        frame_reservas.place(y=50)
        frame_scroll = ScrollableFrame(frame_reservas)
        frame_scroll.pack_propagate(False)
        frame_scroll.pack(expand=True, fill=tk.BOTH)

        frame_sub_reserva = []
        reservas_list = self.controller.model.reserva_list
        subtotal = 0
        descuento = 0

        for i in range(len(reservas_list)):
            j = reservas_list[i]
            frame_sub_reserva.append(ttk.Frame(frame_scroll.scrollable_frame, width=435, height=125))
            frame_sub_reserva[-1].config(relief=tk.SOLID, borderwidth=2)
            frame_sub_reserva[-1].grid_propagate(False)
            frame_sub_reserva[-1].pack(pady=5, padx=5)

            frame = frame_sub_reserva[-1]

            ttk.Label(frame, text="Region:", font=self.FONT_MEDIUM).grid(row=0, column=0, sticky=tk.E)
            region_txt = str(j.tipo_region) + " de " + str(j.nombre_region)
            ttk.Label(frame, text=region_txt, font=self.FONT_SMALL).grid(row=0, column=1, columnspan=3, sticky=tk.W)

            ttk.Label(frame, text="Zona:", font=self.FONT_MEDIUM).grid(row=1, column=0, sticky=tk.E)
            ttk.Label(frame, text=j.zona.nombre, font=self.FONT_SMALL).grid(row=1, column=1, columnspan=3, sticky=tk.W)

            ttk.Label(frame, text="Precio:", font=self.FONT_MEDIUM).grid(row=2, column=0, sticky=tk.E)
            ttk.Label(frame, text="$" + str(j.zona.precio), font=self.FONT_SMALL).grid(row=2, column=1, sticky=tk.W)

            ttk.Label(frame, text="Adultos:", font=self.FONT_MEDIUM).grid(row=2, column=2, sticky=tk.E)
            ttk.Label(frame, text=j.personas, font=self.FONT_SMALL).grid(row=2, column=3, sticky=tk.W)

            ttk.Label(frame, text="Sub-Total:", font=self.FONT_MEDIUM).grid(row=3, column=0, sticky=tk.E)
            ttk.Label(frame, text="$" + str(j.subtotal), font=self.FONT_SMALL).grid(row=3, column=1, sticky=tk.W)

            ttk.Label(frame, text="Descuento:", font=self.FONT_MEDIUM).grid(row=4, column=0, sticky=tk.E)
            ttk.Label(frame, text="$" + str(j.descuento), font=self.FONT_SMALL).grid(row=4, column=1, sticky=tk.W)

            ttk.Button(frame, text="CANCELAR", command=lambda k=i: self.handle_cancelar_button(k)).place(x=300, y=80)

            subtotal += j.subtotal
            descuento += j.descuento

        self.add_variable("total_var", subtotal - descuento)

        # Cliente
        frame_cliente = ttk.LabelFrame(self.frame, text="Informacion Cliente", width=345, height=200)
        frame_cliente.grid_propagate(False)
        frame_cliente.place(x=480, y=50)

        entries_strings = ["Nombre:", "Cedula:", "Edad:", "Sexo:", "Nacionalidad:", "Telefono:"]

        c = self.controller.get_obj_act(Tipos.CLIENTE).get_attr_list()
        for i in range(len(entries_strings)):
            j = entries_strings[i]
            ttk.Label(frame_cliente, text=j, font=self.FONT_SMALL).grid(row=i, column=0, sticky=tk.E)

            if j == "Sexo:":
                s = tk.StringVar()
                s.set(c[i])
                om = tk.OptionMenu(frame_cliente, s, *['M', 'F', 'OTRO'])
                om.config(relief=tk.SOLID, state=tk.DISABLED)
                om.grid(row=i, column=1, sticky=tk.W)
                if self.controller.get_obj_act(Tipos.CLIENTE).jubilado:
                    label = ttk.Label(frame_cliente, text="Si", font=self.FONT_SMALL, foreground=self.green)
                else:
                    label = ttk.Label(frame_cliente, text="No", font=self.FONT_SMALL, foreground=self.red)
                label.grid(row=i - 1, column=1, sticky=tk.W, padx=95)
                continue

            entry = ttk.Entry(frame_cliente, textvariable=c[i])
            entry.delete(0, 'end')
            entry.insert(0, c[i])
            entry.config(state=tk.DISABLED)
            entry.grid(row=i, column=1, sticky=tk.W, pady=3)

            if j == "Edad:":
                entry.config(width=5)
                ttk.Label(frame_cliente, text="Jubilado:", font=self.FONT_SMALL).grid(row=i, column=1, sticky=tk.W, padx=40)

        # Total
        frame_total = ttk.LabelFrame(self.frame, text="Informacion Pago", width=345, height=250)
        frame_total.grid_propagate(False)
        frame_total.place(x=480, y=260)

        ttk.Label(frame_total, text="Total de Reservas:", font=self.FONT_MEDIUM).grid(row=0, column=0, columnspan=3, sticky=tk.E)
        ttk.Label(frame_total, text=len(reservas_list), font=self.FONT_SMALL).grid(row=0, column=3, sticky=tk.W)

        ttk.Label(frame_total, text="Sub-Total:", font=self.FONT_MEDIUM).grid(row=1, column=0, sticky=tk.E)
        ttk.Label(frame_total, text="$" + str(subtotal), font=self.FONT_SMALL).grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame_total, text="Descuento:", font=self.FONT_MEDIUM).grid(row=2, column=0, sticky=tk.E)
        ttk.Label(frame_total, text="$" + str(descuento), font=self.FONT_SMALL).grid(row=2, column=1, sticky=tk.W)

        ttk.Label(frame_total, text="Total:", font=self.FONT_MEDIUM).grid(row=3, column=0, sticky=tk.E)
        ttk.Label(frame_total, text="$" + str(self.get_variable("total_var")), font=self.FONT_SMALL).grid(row=3, column=1, sticky=tk.W)

        ttk.Label(frame_total, text="", font=self.FONT_MEDIUM).grid(row=4, column=0)

        ttk.Label(frame_total, text="Total Abonado:", font=self.FONT_MEDIUM).grid(row=5, column=0, columnspan=2, sticky=tk.E)
        abono_label = ttk.Label(frame_total, text="$0", font=self.FONT_SMALL)
        abono_label.grid(row=5, column=2, columnspan=2, sticky=tk.W)
        self.add_widget("abono_label", abono_label)

        ttk.Label(frame_total, text="Total Adeudado:", font=self.FONT_MEDIUM).grid(row=6, column=0, columnspan=2, sticky=tk.E)
        deuda_label = ttk.Label(frame_total, text="$" + str(self.get_variable("total_var")), font=self.FONT_SMALL)
        deuda_label.grid(row=6, column=2, columnspan=2, sticky=tk.W)
        self.add_widget("deuda_label", deuda_label)

        abono_var = tk.StringVar()
        abono_var.set("0")
        self.add_variable("abono_var", abono_var)

        ttk.Label(frame_total, text="Abono:", font=self.FONT_SMALL).grid(row=5, column=4, sticky=tk.W, pady=5)
        ttk.Entry(frame_total, textvariable=abono_var, width=8).grid(row=5, column=5, sticky=tk.W, padx=5)

        ttk.Button(frame_total, text="ABONAR", command=self.handle_abono_button).grid(row=6, column=4, columnspan=2)
        ttk.Button(frame_total, text="CONFIRMAR RESERVAS", command=self.handle_confirm_button).place(x=50, y=180)

    def handle_back_button(self):
        self.create_mapa_window()

    def handle_cancelar_button(self, index):
        if messagebox.askyesno("Mensaje", "Seguro que desea cancelar esta reserva?"):
            self.controller.pop_reserva(index)
            if len(self.controller.get_reservalist()) == 0:
                messagebox.showwarning("Warning", "No tiene ninguna reserva activa")
                self.controller.clear_reservalist()
                self.create_mapa_window()
            else:
                self.create_pagar_window()
        else:
            return

    def handle_abono_button(self):
        try:
            abono_int = int(self.get_variable("abono_var").get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese solo numeros")
            return

        if abono_int <= 0:
            messagebox.showwarning("Warning", "El abono tien que mayor que 0")
            return

        if abono_int > self.get_variable("total_var"):
            messagebox.showwarning("Warning", "El abono no puede ser mas que el total")
            return

        self.get_widget("abono_label").config(text="$" + str(abono_int))
        self.get_widget("deuda_label").config(text="$" + str(self.get_variable("total_var") - abono_int))

    def handle_confirm_button(self):
        if messagebox.askyesno("Mensaje", "Seguro que desea confirmar su reserva?"):
            messagebox.showinfo("Gracias", "Disfrute sus vacaiones!")
            self.controller.clear_reservalist()
            self.create_mapa_window()

    def create_mapa_window(self):
        self.controller.create_mapa_view()

    def create_pagar_window(self):
        self.controller.create_pagar_view()


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")