import os
from tkinter import *
from tkinter import messagebox, ttk, scrolledtext as st
from tkinter.font import Font

from PIL import ImageTk, Image


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
        self.font_stu = Font(family='Courier', size=12, weight='bold', underline=True)
        self.font_b = Font(family='Courier', size=10)

        self.total_var = []
        for i in range(3):
            self.total_var.append(StringVar())

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
        Label(self.frame, text="Wyming Zeng - 8-966-1043", font=self.font_st).grid(row=12)

        Label(self.frame, text="Profesor:", font=self.font_st, height=2).grid(row=13)
        Label(self.frame, text="Ing. Samuel Jiménez", font=self.font_st).grid(row=14)

        Label(self.frame, text="SEMESTRE II, 2020", font=self.font_st, height=2).grid(row=15)

        Button(self.frame, text="EMPEZAR", bg=c_yellow, command=lambda: self.show_main_window()).grid(row=16)
        Label(self.frame, text="").grid(row=17)

    # Main window
    def show_main_window(self):
        self.init_self_frame()

        Label(self.frame, text="ELIJA SU DESTINO", font=self.font_t, height=2).grid(row=0, column=0, columnspan=2)

        mapa = Canvas(self.frame, height=400, width=800)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img = ImageTk.PhotoImage(Image.open(str(dir_path) + '/img/panama.png'))
        mapa.image = img
        mapa.create_image(400, 200, image=img)
        mapa.grid(row=1, column=0)

        self.create_provincias_text(mapa)
        self.create_comarcas_text(mapa)

        mapa.tag_bind("p", "<Button-1>", self.on_canvas_click)
        mapa.tag_bind("c", "<Button-1>", self.on_canvas_click)

        Label(self.frame, text="MOSTAR: ", font=self.font_st, height=3).grid(row=3, column=0, sticky=W)

        self.display_var.set(0)
        Radiobutton(self.frame, text="SOLO PROVINCIAS", value=2, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=75)
        Radiobutton(self.frame, text="SOLO COMARCAS", value=1, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=200)
        Radiobutton(self.frame, text="AMBAS", value=0, variable=self.display_var,
                    command=lambda: self.change_display_mode(mapa)).grid(row=3, column=0, sticky=W, padx=325)

        frame_b = LabelFrame(self.frame, borderwidth=0, highlightthickness=0)
        frame_b.place(x=630, y=470)
        # Botones
        Button(frame_b, text="CANCELAR RESERVAS", bg=c_yellow,
               command=self.cancelar_reservas, height=2).grid(row=0, column=0)
        Button(frame_b, text="PAGAR", bg=c_yellow,
               command=self.show_pagar_window, height=2).grid(row=0, column=1, padx=10)

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

        try:
            r = w.itemcget(*i, "text")
        except TclError:
            return

        r = r.replace("\n", " ")

        self.controller.set_regionact_by_nombre(r)
        self.show_sub_window()

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
            self.controller.model.cliente_act = None

    # sub windows
    def init_self_frame(self):
        self.frame.destroy()
        self.root.geometry("900x600")

        self.frame = LabelFrame(self.root, borderwidth=5, relief=SOLID, pady=10, padx=10)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)

    def show_sub_window(self):
        # Init
        self.init_self_frame()

        model = self.controller.model

        Button(self.frame, text="\u21E6 ATRAS", bg=c_yellow,
               command=lambda: self.show_main_window() if model.zona_act is None else
               self.sub_change_objact(model.region_act)).place(x=0, y=0)

        dir_path = os.path.dirname(os.path.realpath(__file__))

        if model.zona_act is None:
            act = model.region_act
            frame3_titulo = "Zonas Turisticas"
            img_path = str(dir_path) + '/img/mapas/' + str(model.region_act.nombre) + '.png'
        else:
            act = model.zona_act
            frame3_titulo = "Incluye"
            self.controller.set_zonaact(act)
            img_path = str(dir_path) + '/img/zonas/' + str(model.region_act.nombre) + '/' + str(
                model.zona_act.nombre) + '.png'

        # Titulo
        Label(self.frame, text="ELIJA SU DESTINO", font=self.font_t).pack()
        Label(self.frame, text=act.nombre, font=self.font_st).pack()

        # # Frames
        # Imagen
        frame_foto = create_frame(self.frame, "", 475, 475)
        frame_foto.place(y=50)

        img = ImageTk.PhotoImage(Image.open(img_path))

        canvas = Canvas(frame_foto, width=475, height=475)
        canvas.pack(expand=YES, fill=BOTH)

        canvas.image = img
        canvas.create_image(237, 237, image=img, anchor=CENTER)

        # Descripcion
        frame_desc = create_frame(self.frame, "Descripcion", 350, 230)
        frame_desc.pack_propagate(False)
        frame_desc.place(x=475, y=50)

        descripcion_box = st.ScrolledText(frame_desc, font=self.font_b, wrap=WORD, borderwidth=1, highlightthickness=1)
        descripcion_box.insert(INSERT, act.desc)
        descripcion_box.config(state=DISABLED)
        descripcion_box.pack(expand=True, fill=BOTH)

        # Zonas/Extras
        frame3 = create_frame(self.frame, frame3_titulo, 350, 230)
        frame3.place(x=475, y=290)

        if model.zona_act is None:
            zonas = act.zonas
            for i in zonas:
                Button(frame3, text=i.nombre, bg=c_light_blue,
                       command=lambda j=i: self.sub_change_objact(j), height=2, width=40).pack(pady=5)
        else:
            frame3.config(height=190)
            extras_box = st.ScrolledText(frame3, font=self.font_b, wrap=WORD, borderwidth=1,
                                         highlightthickness=1)
            extras_box.insert(INSERT, act.extras)
            extras_box.config(state=DISABLED)
            extras_box.pack(expand=True, fill=BOTH)

            precio_frame = create_frame(self.frame, "", 350, 45)
            precio_frame.place(x=475, y=480)

            Label(precio_frame, text="Precio: $" + str(act.precio), font=self.font_st).place(y=10)
            Button(precio_frame, text="RESERVAR", bg=c_yellow, command=self.show_reservar_window).place(x=275, y=10)

    def sub_change_objact(self, obj):
        self.controller.set_objact(obj)
        self.show_sub_window()

    def show_reservar_window(self):
        self.init_self_frame()

        model = self.controller.model

        Button(self.frame, text="\u21E6 ATRAS", bg=c_yellow,
               command=lambda: self.sub_change_objact(model.zona_act)).place(x=5, y=5)

        cant_var = StringVar()
        cant_var.set("1")
        cant_var.trace('w', lambda a, b, c: self.check_cant(cant_var))

        # Titulo
        Label(self.frame, text="CONFIRMAR RESERVA", font=self.font_t, relief=SOLID).pack()

        # # Frames
        # Destino
        frame_destino = create_frame(self.frame, "Informacion Destino", 800, 100)
        frame_destino.grid_propagate(False)
        frame_destino.pack(pady=5)

        Label(frame_destino, text="Region:", font=self.font_stu).grid(row=0, column=0, sticky=E)
        region_txt = str(model.region_act.get_tipo_nombre()) + " de " + str(model.region_act.nombre)
        Label(frame_destino, text=region_txt, font=self.font_st).grid(row=0, column=1, sticky=W)

        Label(frame_destino, text="Zona:", font=self.font_stu).grid(row=1, column=0, sticky=E)
        Label(frame_destino, text=model.zona_act.nombre, font=self.font_st).grid(row=1, column=1, sticky=W)

        Label(frame_destino, text="Precio:", font=self.font_stu).grid(row=2, column=0, sticky=E)
        Label(frame_destino, text="$" + str(model.zona_act.precio), font=self.font_st).grid(row=2, column=1, sticky=W)

        # Cliente
        frame_cliente = create_frame(self.frame, "Informacion Cliente", 400, 300)
        frame_cliente.grid_propagate(False)
        frame_cliente.place(y=150)

        entries_strings = ["Nombre:", "Cedula:", "Edad:", "Sexo:", "Nacionalidad:", "Telefono:"]
        entries_vars = []

        for i in range(len(entries_strings)):
            j = entries_strings[i]
            Label(frame_cliente, text=j, font=self.font_stu, height=2).grid(row=i, column=0, sticky=E)
            entries_vars.append(StringVar())

            if j == "Sexo:":
                om = OptionMenu(frame_cliente, entries_vars[-1], *['M', 'F', 'OTRO'])
                om.config(relief=SOLID)
                om.grid(row=i, column=1, sticky=W)
                label = Label(frame_cliente, text="No", fg=c_red)
                label.grid(row=i - 1, column=1, sticky=W, padx=90)
                entries_vars[2].trace('w', lambda a, b, c: self.check_jubilado(entries_vars[2], entries_vars[3], label))
                entries_vars[3].trace('w', lambda a, b, c: self.check_jubilado(entries_vars[2], entries_vars[3], label))
                continue

            entry = Entry(frame_cliente, textvariable=entries_vars[-1], relief=SOLID)
            entry.grid(row=i, column=1, sticky=W)

            if j == "Edad:":
                entry.config(width=5)
                entries_vars[-1].set("18")
                Label(frame_cliente, text="Jubilado:").grid(row=i, column=1, sticky=W, padx=40)

        if model.cliente_act is not None:
            c = model.cliente_act.get_attr_list()
            for i, j in zip(entries_vars, c):
                i.set(j)
            widgets = frame_cliente.winfo_children()
            for i in widgets:
                j = i.winfo_class()
                if j == "Entry" or j == "Menubutton":
                    i.config(state=DISABLED)

        # Pago
        frame_pago = create_frame(self.frame, "Informacion Pago", 400, 300)
        frame_pago.grid_propagate(False)
        frame_pago.place(x=420, y=150)

        Label(frame_pago, text="Adultos:", font=self.font_stu, height=2).grid(row=0, column=0, sticky=E)
        Entry(frame_pago, textvariable=cant_var, relief=SOLID, width=5).grid(row=0, column=1, sticky=W)

        Label(frame_pago, text="Sub-Total:", font=self.font_stu, height=2).grid(row=1, column=0, sticky=E)
        Label(frame_pago, text="Descuento:", font=self.font_stu, height=2).grid(row=2, column=0, sticky=E)
        Label(frame_pago, text="Total:", font=self.font_stu, height=2).grid(row=3, column=0, sticky=E)

        for i in range(len(self.total_var)):
            Entry(frame_pago, textvariable=self.total_var[i], relief=SOLID, state=DISABLED)\
                .grid(row=i+1, column=1, sticky=W)

        Button(frame_pago, text="CANCELAR", bg=c_yellow,
               command=lambda: self.show_main_window() if show_yesnobox("Desea cancelar y volver al menu principal?")
               else None, height=2).place(x=5, y=230)
        Button(frame_pago, text="CONFIRMAR RESERVA", bg=c_yellow,
               command=lambda: self.check_confirmar_reserva(entries_vars), height=2) \
            .place(x=250, y=230)

        self.controller.update_work_vars()
        self.refresh_totals()

    def check_jubilado(self, edad, sexo, label):
        if edad.get() == "":
            return

        try:
            e = int(edad.get())
        except ValueError:
            show_warningbox("La edad solo puede ser un numero")
            edad.set("18")
            return

        if e >= 57 and sexo.get() == "F":
            label.config(text="Si", fg=c_green)
            self.controller.work_es_jubilado = True
        elif e >= 62 and sexo.get() == "M":
            label.config(text="Si", fg=c_green)
            self.controller.work_es_jubilado = True
        else:
            label.config(text="No", fg=c_red)
            self.controller.work_es_jubilado = False

        self.controller.update_work_vars()
        self.refresh_totals()

    def check_cant(self, cant):
        if cant.get() == "":
            return

        try:
            e = int(cant.get())
        except ValueError:
            show_warningbox("La cantidad de personas debe ser un numero")
            cant.set(self.controller.work_cant)
            return

        if e <= 0 or e > 10:
            show_warningbox("La cantidad de personas debe ser mayor que 0 y menor que 10")
            cant.set(self.controller.work_cant)
            return

        self.controller.work_cant = e
        self.controller.update_work_vars()
        self.refresh_totals()

    def refresh_totals(self):
        self.total_var[0].set("$" + str(self.controller.work_subtotal))
        self.total_var[1].set("$" + str(self.controller.work_descuento))
        self.total_var[2].set("$" + str(self.controller.work_subtotal - self.controller.work_descuento))

    def check_confirmar_reserva(self, entries_vars):
        for i in entries_vars:
            if i.get() == "":
                show_warningbox("Los campos de informacion del cliente no pueden estar vacios")
                return

        if int(entries_vars[2].get()) < 18:
            show_warningbox("La edad tiene que ser mayor que 18")
            entries_vars[2].set("18")
            return

        if self.controller.model.cliente_act is None:
            e = []
            for i in entries_vars:
                e.append(i.get())
            self.controller.set_cliente_act(e)

        self.controller.add_reserva()

        r = show_yesnobox("Desea agregar otra reserva?")
        if r:
            self.show_main_window()
        else:
            self.show_pagar_window()

    def show_pagar_window(self):
        if len(self.controller.model.reserva_list) == 0:
            show_warningbox("No tiene ninguna reserva activa")
            return

        self.init_self_frame()

        Button(self.frame, text="\u21E6 ATRAS", bg=c_yellow,
               command=self.show_main_window).place(x=0, y=0)

        Label(self.frame, text="PAGAR", font=self.font_t, relief=SOLID).pack()

        # # Frames
        # Reservas
        frame_reservas = create_frame(self.frame, "", 475, 475)
        frame_reservas.config(relief=SOLID, bd=2)
        frame_reservas.place(y=50)
        frame_scroll = ScrollableFrame(frame_reservas)
        frame_scroll.pack_propagate(False)
        frame_scroll.pack(expand=True, fill=BOTH)

        frame_sub_reserva = []
        reservas_list = self.controller.model.reserva_list
        subtotal = 0
        descuento = 0

        for i in range(len(reservas_list)):
            j = reservas_list[i]
            frame_sub_reserva.append(create_frame(frame_scroll.scrollable_frame, "", 435, 125))
            frame_sub_reserva[-1].config(relief=SOLID, bd=2)
            frame_sub_reserva[-1].grid_propagate(False)
            frame_sub_reserva[-1].pack(pady=5, padx=5)

            frame = frame_sub_reserva[-1]

            Label(frame, text="Region:", font=self.font_st).grid(row=0, column=0, sticky=E)
            region_txt = str(j.tipo_region) + " de " + str(j.nombre_region)
            Label(frame, text=region_txt, font=self.font_b).grid(row=0, column=1, columnspan=3, sticky=W)

            Label(frame, text="Zona:", font=self.font_st).grid(row=1, column=0, sticky=E)
            Label(frame, text=j.zona.nombre, font=self.font_b).grid(row=1, column=1, columnspan=3, sticky=W)

            Label(frame, text="Precio:", font=self.font_st).grid(row=2, column=0, sticky=E)
            Label(frame, text="$" + str(j.zona.precio), font=self.font_b).grid(row=2, column=1, sticky=W)

            Label(frame, text="Adultos:", font=self.font_st).grid(row=2, column=2, sticky=E)
            Label(frame, text=j.personas, font=self.font_b).grid(row=2, column=3, sticky=W)

            Label(frame, text="Sub-Total:", font=self.font_st).grid(row=3, column=0, sticky=E)
            Label(frame, text="$" + str(j.subtotal), font=self.font_b).grid(row=3, column=1, sticky=W)

            Label(frame, text="Descuento:", font=self.font_st).grid(row=4, column=0, sticky=E)
            Label(frame, text="$" + str(j.descuento), font=self.font_b).grid(row=4, column=1, sticky=W)

            Button(frame, text="CANCELAR", bg=c_red, relief=SOLID,
                   command=lambda k=i: self.remove_reserva(k)).place(x=355, y=90)

            subtotal += j.subtotal
            descuento += j.descuento

        # Cliente
        frame_cliente = create_frame(self.frame, "Informacion Cliente", 345, 200)
        frame_cliente.grid_propagate(False)
        frame_cliente.place(x=480, y=50)

        entries_strings = ["Nombre:", "Cedula:", "Edad:", "Sexo:", "Nacionalidad:", "Telefono:"]

        c = self.controller.model.cliente_act.get_attr_list()
        for i in range(len(entries_strings)):
            j = entries_strings[i]
            Label(frame_cliente, text=j, font=self.font_b, height=1).grid(row=i, column=0, sticky=E)

            if j == "Sexo:":
                s = StringVar()
                s.set(c[i])
                om = OptionMenu(frame_cliente, s, *['M', 'F', 'OTRO'])
                om.config(relief=SOLID, state=DISABLED)
                om.grid(row=i, column=1, sticky=W)
                if self.controller.model.cliente_act.jubilado:
                    label = Label(frame_cliente, text="Si", fg=c_green)
                else:
                    label = Label(frame_cliente, text="No", fg=c_red)
                label.grid(row=i - 1, column=1, sticky=W, padx=90)
                continue

            entry = Entry(frame_cliente, textvariable=c[i], relief=SOLID)
            entry.delete(0, 'end')
            entry.insert(0, c[i])
            entry.config(state=DISABLED)
            entry.grid(row=i, column=1, sticky=W)

            if j == "Edad:":
                entry.config(width=5)
                Label(frame_cliente, text="Jubilado:").grid(row=i, column=1, sticky=W, padx=40)

        # Total
        frame_total = create_frame(self.frame, "Informacion Pago", 345, 250)
        frame_total.grid_propagate(False)
        frame_total.place(x=480, y=260)

        Label(frame_total, text="Total de Reservas:", font=self.font_stu).grid(row=0, column=0, columnspan=3, sticky=E)
        Label(frame_total, text=len(reservas_list), font=self.font_b).grid(row=0, column=3, sticky=W)

        Label(frame_total, text="Sub-Total:", font=self.font_stu).grid(row=1, column=0, sticky=E)
        Label(frame_total, text="$" + str(subtotal), font=self.font_b).grid(row=1, column=1, sticky=W)

        Label(frame_total, text="Descuento:", font=self.font_stu).grid(row=2, column=0, sticky=E)
        Label(frame_total, text="$" + str(descuento), font=self.font_b).grid(row=2, column=1, sticky=W)

        total = subtotal - descuento

        Label(frame_total, text="Total:", font=self.font_stu).grid(row=3, column=0, sticky=E)
        Label(frame_total, text="$" + str(total), font=self.font_b).grid(row=3, column=1, sticky=W)

        Label(frame_total, text="", font=self.font_stu).grid(row=4, column=0)

        labels = []

        Label(frame_total, text="Total Abonado:", font=self.font_stu).grid(row=5, column=0, columnspan=2, sticky=E)
        labels.append(Label(frame_total, text="$0", font=self.font_b))
        labels[-1].grid(row=5, column=2, sticky=W)

        Label(frame_total, text="Total Adeudado:", font=self.font_stu).grid(row=6, column=0, columnspan=2, sticky=E)
        labels.append(Label(frame_total, text="$" + str(total), font=self.font_b))
        labels[-1].grid(row=6, column=2, sticky=W)

        abono_var = StringVar()
        abono_var.set("0")

        Label(frame_total, text="Abono:", font=self.font_b).grid(row=7, column=0, sticky=W, pady=5)
        Entry(frame_total, relief=SOLID, textvariable=abono_var, width=10).grid(row=8, column=0, sticky=W, padx=5)

        Button(frame_total, text="ABONAR", bg=c_yellow,
               command=lambda: self.check_abono(abono_var, total, labels),
               height=2, width=15).place(x=75, y=180)
        Button(frame_total, text="CONFIRMAR RESERVAS", bg=c_yellow,
               command=lambda: self.confirm_reserva(), height=2, width=18).place(x=200, y=180)

    def remove_reserva(self, index):
        if show_yesnobox("Seguro que desea cancelar esta reserva?"):
            self.controller.remove_reserva(index)
            if len(self.controller.model.reserva_list) == 0:
                show_warningbox("No tiene ninguna reserva activa")
                self.controller.clear_reservas()
                self.show_main_window()
            else:
                self.show_pagar_window()
        else:
            return

    def check_abono(self, abono, total, labels):
        try:
            abono_int = int(abono.get())
        except ValueError:
            show_warningbox("Ingrese solo numeros")
            return

        if abono_int <= 0:
            show_warningbox("El abono tien que mayor que 0")
            return

        if abono_int > total:
            show_warningbox("El abono no puede ser mas que el total")
            return

        labels[0].config(text="$" + str(abono_int))
        labels[1].config(text="$" + str(total - abono_int))

    def confirm_reserva(self):
        if show_yesnobox("Seguro que desea confirmar su reserva?"):
            messagebox.showinfo("Gracias", "Disfrute sus vacaiones!")
            self.controller.clear_reservas()
            self.show_main_window()


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        gui_style = ttk.Style()
        gui_style.configure('My.TFrame', background=c_white)
        self.scrollable_frame = ttk.Frame(canvas, style='My.TFrame')

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


# funciones
def create_frame(parent, text, width, height):
    # , relief=SOLID,  borderwidth=1
    if text == "":
        frame = Frame(parent, width=width, height=height)
    else:
        frame = LabelFrame(parent, text=text, width=width, height=height, relief=SOLID)
    frame.pack_propagate(False)
    return frame


def show_warningbox(msg):
    messagebox.showwarning("Warning", msg)


def show_yesnobox(msg):
    return messagebox.askyesno("Mensaje", msg)


# Colores
c_black = '#000000'
c_white = '#FFFFFF'
c_yellow = '#ffee58'
# c_blue = '#0336FF'
c_blue = "#7986cb"
# c_light_blue = "#03b3ff"
c_light_blue = "#82b1ff"
c_pink = '#FF0266'
c_red = '#ef5350'
c_green = '#41c300'
