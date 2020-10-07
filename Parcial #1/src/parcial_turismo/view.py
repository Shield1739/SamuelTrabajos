import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

from PIL import ImageTk, Image

import parcial_turismo as pt
from parcial_turismo import *


class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.configure(background=c_blue)

        self.frame = LabelFrame(self.root)

        self.display_var = IntVar()

        # Fonts
        self.font_t = Font(family='Courier', size=15, weight='bold')
        self.font_st = Font(family='Courier', size=12, weight='bold')
        self.font_b = Font(family='Courier', size=10)

        self.subtotal_label = Label()
        self.descuento_label = Label()
        self.total_label = Label()

        self.show_presentacion_window()

    def show_presentacion_window(self):
        self.frame.config(borderwidth=4, relief=SOLID)
        self.frame.pack(pady=25)
        self.root.geometry("600x600")

        Label(self.frame, text="UNIVERSIDAD TECNOLÓGICA DE PANAMÁ", font=self.font_st).grid(row=0)
        Label(self.frame, text="FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES", font=self.font_st).grid(row=1)
        Label(self.frame, text="DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS", font=self.font_st).grid(row=2)
        Label(self.frame, text="CARRERA LICENCIATURA EN INGENIERÍA DE SOFTWARE", font=self.font_st).grid(row=3)
        Label(self.frame, text="INTRODUCCIÓN A LA TEORÍA COMPUTACIONAL", font=self.font_st).grid(row=4)

        Label(self.frame, text="PARCIAL & PROYECTO #1", font=self.font_st, height=4).grid(row=6)

        Label(self.frame, text="INTEGRANTES:", font=self.font_st, height=3).grid(row=7)
        Label(self.frame, text="Kevin Feng - 3-748-410", font=self.font_st).grid(row=8)
        Label(self.frame, text="Angel Iglesias - 8-958-1", font=self.font_st).grid(row=9)
        Label(self.frame, text="Sahori Raby - 8-964-644", font=self.font_st).grid(row=10)
        Label(self.frame, text="Luis Villalaz - 8-925-2287", font=self.font_st).grid(row=11)
        Label(self.frame, text="Wymming Zheng - 8-966-1043", font=self.font_st).grid(row=12)

        Label(self.frame, text="Profesor:", font=self.font_st, height=2).grid(row=13)
        Label(self.frame, text="Ing. Samuel Jiménez", font=self.font_st).grid(row=14)

        Label(self.frame, text="SEMESTRE II, 2020", font=self.font_st, height=2).grid(row=15)

        Button(self.frame, text="EMPEZAR", bg=c_yellow, command=lambda: self.show_main_window()).grid(row=16)
        Label(self.frame, text="").grid(row=17)

    # Main window
    def show_main_window(self):
        self.frame.destroy()
        self.root.geometry("900x600")

        self.frame = LabelFrame(self.root, borderwidth=4, relief=SOLID)
        self.frame.pack(pady=20)

        Label(self.frame, text="ELIGA SU DESTINO", font=self.font_t, height=2).grid(row=0, column=0, columnspan=2)

        mapa = Canvas(self.frame, height=400, width=800)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img = ImageTk.PhotoImage(Image.open(str(dir_path) + '/img/panama.png'))
        mapa.image = img
        mapa.create_image(400, 200, image=img)
        mapa.grid(row=1, column=0)

        self.create_provincias_text(mapa)
        self.create_comarcas_text(mapa)

        mapa.tag_bind("p", "<ButtonRelease-1>", self.on_canvas_click)
        mapa.tag_bind("c", "<ButtonRelease-1>", self.on_canvas_click)

        Label(self.frame, text="MOSTAR: ", font=self.font_st, height=5).grid(row=3, column=0, sticky=W)

        self.display_var.set(0)
        Radiobutton(self.frame, text="SOLO PROVINCIAS", value=2, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=75)
        Radiobutton(self.frame, text="SOLO COMARCAS", value=1, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=200)
        Radiobutton(self.frame, text="AMBAS", value=0, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=325)

        frame_b = LabelFrame(self.frame, borderwidth=0, highlightthickness=0)
        frame_b.place(x=600, y=490)
        # Botones
        Button(frame_b, text="CANCELAR RESERVAS", bg=c_yellow,
               command=self.cancelar_reservas, height=2).grid(row=0, column=0)
        Button(frame_b, text="PAGAR", bg=c_yellow,
               command=lambda: print("DO PAGAR WINDOW"), height=2).grid(row=0, column=1, padx=10)

    def change_display_mode(self, mapa):
        mapa.delete("p")
        mapa.delete("c")
        e = self.display_var.get()
        if e == 2:
            self.create_provincias_text(mapa)
        elif e == 1:
            self.create_comarcas_text(mapa)
        else:
            self.create_provincias_text(mapa)
            self.create_comarcas_text(mapa)

    def on_canvas_click(self, event):
        w = event.widget
        i = w.find_closest(event.x, event.y)

        r = w.itemcget(*i, "text")
        r = r.replace("\n", " ")

        self.controller.set_regionact_by_nombre(r)
        self.show_sub_window(self.controller.model.region_act)

    def create_provincias_text(self, mapa):
        canvas_text_provincias = [mapa.create_text(75, 100, text='BOCAS\nDEL TORO'),
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
            mapa.itemconfig(i, fill=c_blue, activefill=c_pink, tag='p', font=self.font_st)

    def create_comarcas_text(self, mapa):
        canvas_text_comarcas = [mapa.create_text(195, 175, text='NGÖBE-BUGLÉ'),
                                mapa.create_text(650, 80, text='GUNA YALA'),
                                mapa.create_text(730, 200, text='EMBERÁ')]

        for i in canvas_text_comarcas:
            mapa.itemconfig(i, fill=c_blue, activefill=c_pink, tag='c', font=self.font_st)

    def cancelar_reservas(self):
        if len(self.controller.model.reserva_list) == 0:
            show_warningbox("No tiene ninguna reserva activa")
            return

        v = show_yesnobox("Desea cancelar sus reservas activas?")

        if v:
            self.controller.clear_reservas()

    # sub windows
    def show_sub_window(self, obj):
        # Init
        self.frame.destroy()
        self.root.geometry("800x400")

        self.frame = LabelFrame(self.root, borderwidth=4, relief=SOLID, pady=10, padx=10)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)

        obj_tipo = self.controller.get_tipo_obj(obj)

        Button(self.frame, text="\u21E6 ATRAS", bg=c_yellow,
               command=lambda: self.show_main_window() if obj_tipo == "region" else
               self.show_sub_window(self.controller.model.region_act)).grid(row=0, column=0, sticky=W)

        # Titulos
        Label(self.frame, text=obj.nombre, font=self.font_t).grid(row=0, column=0, columnspan=3)

        # Imagen
        Label(self.frame, text="Foto:", font=self.font_st).grid(row=1, column=0, sticky=W)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = ""

        if obj_tipo == "region":
            img_path = str(dir_path) + '/img/mapas/' + str(obj.nombre) + '.png'
        elif obj_tipo == "zona":
            self.controller.set_zonaact(obj)
            m = self.controller.model
            img_path = str(dir_path) + '/img/zonas/' + str(m.region_act.nombre) + '/' + str(m.zona_act.nombre) + '.png'

        img = ImageTk.PhotoImage(Image.open(img_path))

        canvas = Canvas(self.frame, width=250, height=250)
        canvas.image = img
        canvas.create_image(125, 125, image=img)
        canvas.grid(row=2, column=0, rowspan=4, sticky=W)

        # Desc
        Label(self.frame, text="Descripcion:", font=self.font_st).grid(row=1, column=1, sticky=W)

        desc_frame = LabelFrame(self.frame, width=250, height=250)
        desc_frame.grid_rowconfigure(0, weight=1)
        desc_frame.grid_columnconfigure(0, weight=1)
        desc_frame.grid_propagate(False)
        desc_frame.grid(row=2, column=1, rowspan=4, sticky=NSEW)

        # TODO WARP IN FUNC !A
        desc_text = Text(desc_frame, font=self.font_b, wrap=WORD, borderwidth=0, highlightthickness=0)
        desc_text.insert(INSERT, obj.desc)
        desc_text.config(state=DISABLED)
        desc_text.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollbar = Scrollbar(desc_frame, command=desc_text.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        desc_text['yscrollcommand'] = scrollbar.set

        # Zonas / Precios
        if obj_tipo == "region":
            Label(self.frame, text="Zonas Turisticas:", font=self.font_st).grid(row=1, column=2, sticky=W)
            zonas = obj.zonas
            for i in range(len(zonas)):
                z = zonas[i]
                Button(self.frame, text=z.nombre, bg=c_light_blue,
                       command=lambda j=z: self.show_sub_window(j), height=3, width=30).grid(row=i + 2, column=2)
        elif obj_tipo == "zona":
            Label(self.frame, text="Incluye:", font=self.font_st).grid(row=1, column=2, sticky=W)

            extras_frame = LabelFrame(self.frame, width=200, height=250, borderwidth=0, highlightthickness=0)
            extras_frame.grid_rowconfigure(0, weight=1)
            extras_frame.grid_columnconfigure(0, weight=1)
            extras_frame.grid_propagate(False)
            extras_frame.grid(row=2, column=2, rowspan=2, columnspan=2, sticky=NSEW)

            # TODO WARP IN FUNC !A
            extras_text = Text(extras_frame, font=self.font_b, wrap=WORD, borderwidth=0, highlightthickness=0)
            extras_text.insert(INSERT, obj.extras)
            extras_text.config(state=DISABLED)
            extras_text.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

            Label(self.frame, text="Precio: $" + str(obj.precio), font=self.font_st).grid(row=5, column=2, sticky=W)
            Button(self.frame, text="RESERVAR", bg=c_yellow, command=self.show_reservar_window) \
                .grid(row=5, column=3, sticky=W)

    def show_reservar_window(self):
        # Init
        self.frame.destroy()
        self.root.geometry("800x400")

        self.frame = LabelFrame(self.root, borderwidth=4, relief=SOLID)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)

        m = self.controller.model

        # Titulos
        Label(self.frame, text="RESERVAR", font=self.font_t).pack()
        Button(self.frame, text="\u21E6 ATRAS", bg=c_yellow,
               command=lambda: self.show_sub_window(m.zona_act)).place(x=5, y=5)

        # Destino Frame
        frame_t = LabelFrame(self.frame, bg=c_light_blue, height=75, width=725)
        frame_t.grid_propagate(False)
        frame_t.pack(pady=5)

        Label(frame_t, text="DESTINO:", font=self.font_st, bg=c_light_blue).grid(row=0, column=0, sticky=E)
        dt = str(m.zona_act.nombre) + ", " + str(m.region_act.get_tipo_nombre()) + " de " + str(m.region_act.nombre)
        Label(frame_t, text=dt, font=self.font_st, bg=c_light_blue).grid(row=0, column=1, sticky=W)
        Label(frame_t, text="PRECIO:", font=self.font_st, bg=c_light_blue).grid(row=1, column=0, sticky=E)
        Label(frame_t, text="$" + str(m.zona_act.precio) + " por persona", font=self.font_st, bg=c_light_blue).grid(
            row=1, column=1, sticky=W)

        # TODO MAYBE WARP IN FUNC?
        # Cliente frame
        frame_e = LabelFrame(self.frame, bg=c_light_blue, height=175, width=725)
        frame_e.grid_propagate(False)
        frame_e.pack()

        entries = []
        entries_vars = []
        entries_strings = ["Nombre:", "Edad:", "Nacionalidad:", "Es Jubilado?", "Sexo:", "Cedula", "Telefono:"]

        for i in range(2):
            for j in range(4 - i):
                s = entries_strings[j + (i * 4)]
                Label(frame_e, text=s, bg=c_light_blue, font=self.font_b, height=2).grid(row=j, column=i * 2, sticky=E)

                if s == "Es Jubilado?":
                    entries.append(Checkbutton(frame_e, bg=c_light_blue,
                                               offvalue=False, onvalue=True, variable=self.controller.es_jubilado,
                                               command=self.check_totales))
                    entries[-1].grid(row=j, column=i+1, sticky=W)
                    continue

                entries_vars.append(StringVar())
                if s == "Sexo:":
                    entries.append(OptionMenu(frame_e, entries_vars[-1], *['M', 'F', 'OTRO']))
                    entries[-1].config(bd=0)
                    entries[-1].grid(row=j, column=i * 2 + 1, sticky=W)
                    continue

                entries.append(Entry(frame_e, textvariable=entries_vars[-1]))
                entries[-1].grid(row=j, column=i * 2 + 1)
                # entries.append(Entry(frame_e))
                # entries[-1].grid(row=j, column=i*2 + 1)

        # TODO PENSAR MEJOR ESTO
        if m.cliente_act is not None:
            c = m.cliente_act
            entries_vars[0].set(c.nombre)
            entries_vars[1].set(c.edad)
            entries_vars[2].set(c.nacionalidad)
            entries_vars[3].set(c.sexo)
            entries_vars[4].set(c.cedula)
            entries_vars[5].set(c.telefono)
            self.controller.es_jubilado.set(c.jubilado)

            for i in entries:
                i.config(state=DISABLED)

        Label(frame_e, text="# de Personas:", bg=c_light_blue, font=self.font_b, height=2)\
            .grid(row=0, column=5, sticky=E)
        cantidad = Entry(frame_e, textvariable=self.controller.cant_var, width=5)
        self.controller.cant_var.trace("w", self.check_totales)
        cantidad.grid(row=0, column=6, sticky=W)

        Label(frame_e, text="Abono:", bg=c_light_blue, font=self.font_b, height=2).grid(row=1, column=5, sticky=E)
        abono = Entry(frame_e, textvariable="$" + str(self.controller.abono_var), width=10)
        # self.controller.cant_var.trace("w", self.update_total)
        abono.grid(row=1, column=6, sticky=W)

        # Totals
        self.controller.update_totales()

        Label(frame_e, text="Sub-Total:", bg=c_light_blue, font=self.font_b).grid(row=2, column=5, sticky=NE)
        self.subtotal_label = Label(frame_e, text="$" + str(self.controller.subtotal), bg=c_light_blue,
                                    font=self.font_b)
        self.subtotal_label.grid(row=2, column=6, sticky=NW)

        Label(frame_e, text="Descuento:", bg=c_light_blue, font=self.font_b).grid(row=2, column=5, sticky=SE)
        self.descuento_label = Label(frame_e, text="$" + str(self.controller.descuento), bg=c_light_blue,
                                     font=self.font_b)
        self.descuento_label.grid(row=2, column=6, sticky=SW)

        Label(frame_e, text="Total:", bg=c_light_blue, font=self.font_b).grid(row=3, column=5, sticky=NE)
        self.total_label = Label(frame_e, text="$" + str(self.controller.subtotal - self.controller.descuento),
                                 bg=c_light_blue, font=self.font_b)
        self.total_label.grid(row=3, column=6, sticky=NW)

        frame_b = LabelFrame(self.frame, borderwidth=0, highlightthickness=0)
        frame_b.place(x=520, y=295)
        # Botones
        Button(frame_b, text="CANCELAR", bg=c_yellow,
               command=lambda: self.show_main_window(), height=2).grid(row=0, column=0)
        Button(frame_b, text="CONFIRMAR RESERVA", bg=c_yellow,
               command=lambda: self.entries_check(entries, True), height=2) \
            .grid(row=0, column=1, padx=10)

    def check_totales(self, *args):
        if self.controller.cant_var.get() == "":
            return

        try:
            cant = int(self.controller.cant_var.get())
        except ValueError:
            show_warningbox("Campo persona debe ser numero")
            self.controller.cant_var.set("1")
            cant = 1

        if cant <= 0:
            show_warningbox("Deben ser 1 o mas personas")
            self.controller.cant_var.set("1")

        self.controller.update_totales()
        self.refresh_totales_labels()

    def refresh_totales_labels(self):
        self.subtotal_label.config(text="$" + str(self.controller.subtotal))
        self.descuento_label.config(text="$" + str(self.controller.descuento))
        self.total_label.config(text="$" + str(self.controller.subtotal - self.controller.descuento))

    def check_cliente_info(self):
        print()

    def show_pagar_window(self):
        self.frame.destroy()
        self.root.geometry("800x400")

        self.frame = LabelFrame(self.root, borderwidth=4, relief=SOLID)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)


# funciones
def show_warningbox(msg):
    messagebox.showwarning("Warning", msg)


# funciones
def show_yesnobox(msg):
    return messagebox.askyesno("Mensaje", msg)


# Globals
Regiones = pt.get_regiones_list()

region_selec = Region(0, 0, 0, 0)
zona_selec = Zona(0, 0, 0, 0)

# Colores
c_black = '#000000'
c_white = '#FFFFFF'
c_p1_m = '#6200EE'
c_p1_v = '#3700B3'
c_p2_m = '#03DAC6'
c_p2_v = '#018786'
c_error = '#B00020'
c_yellow = '#FFCD03'
c_blue = '#0336FF'
c_light_blue = "#03b3ff"
c_pink = '#FF0266'
c_red = '#FF0335'
