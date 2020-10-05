import parcial_turismo as pt
from parcial_turismo import Region, Zona
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import os


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Parcial #1")
        self.geometry("600x600")
        self.resizable(False, False)
        self.configure(background=c_white)

        self.frame = LabelFrame(self, borderwidth=0, highlightthickness=0, bg=c_white)
        self.frame.pack(padx=0, pady=0)

        self.display_var = IntVar()

        self.font_t = Font(family='Courier', size=15, weight='bold')
        self.font_st = Font(family='Courier', size=12, weight='bold')
        self.font_b = Font(family='Courier', size=10)

    def show_presentacion(self):
        Label(self.frame, text="UNI").pack(pady=10)
        Label(self.frame, text="PROYECTO #1").pack(pady=25)

        Label(self.frame, text="NOMBRES").pack(pady=50)

        Label(self.frame, text="II SEMESTRE 2020").pack(pady=100)

        Button(self.frame, text="EMPEZAR", bg=c_black, fg=c_white, command=lambda: self.show_main_window()).pack()
        # TODO KITAR ESTO
        self.show_main_window()

    def show_main_window(self):
        self.frame.destroy()
        self.configure(background=c_black)
        self.geometry("800x600")

        self.frame = LabelFrame(self, borderwidth=0, highlightthickness=0, bg=c_black)
        self.frame.pack()

        Label(self.frame, text="ELIGA SU DESTINO", bg=c_black, fg=c_white, font=self.font_t, height=5)\
            .grid(row=0, column=0, columnspan=2)

        canvas = Canvas(self.frame, height=400, width=800)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img = ImageTk.PhotoImage(Image.open(str(dir_path) + '/img/panama.png'))
        canvas.image = img
        canvas.create_image(400, 200, image=img)
        canvas.grid(row=1, column=0)

        self.create_provincias_text(canvas)
        self.create_comarcas_text(canvas)

        # TODO MAYBE UNRELEASE?
        canvas.bind("<Button-1>", self.on_canvas_click)

        Label(self.frame, text="MOSTAR: ", bg=c_black, fg=c_white, font=self.font_st, height=5) \
            .grid(row=3, column=0, sticky=W)

        self.display_var.set(0)
        Radiobutton(self.frame, text="SOLO PROVINCIAS", bg=c_black, fg=c_white, value=2, variable=self.display_var,
                    command=lambda: self.change_text_display(canvas)).grid(row=3, column=0, sticky=W, padx=75)
        Radiobutton(self.frame, text="SOLO COMARCAS", bg=c_black, fg=c_white, value=1, variable=self.display_var,
                    command=lambda: self.change_text_display(canvas)).grid(row=3, column=0, sticky=W, padx=200)
        Radiobutton(self.frame, text="AMBAS", bg=c_black, fg=c_white, value=0, variable=self.display_var,
                    command=lambda: self.change_text_display(canvas)).grid(row=3, column=0, sticky=W, padx=325)

    # TODO ENCONTRAR MEJOR NOMBRE
    def change_text_display(self, canvas):
        canvas.delete("p")
        canvas.delete("c")
        e = self.display_var.get()
        if e == 2:
            self.create_provincias_text(canvas)
        elif e == 1:
            self.create_comarcas_text(canvas)
        else:
            self.create_provincias_text(canvas)
            self.create_comarcas_text(canvas)

    def create_provincias_text(self, canvas):
        canvas_text_provincias = [canvas.create_text(75, 100, text='BOCAS\nDEL TORO'),
                                  canvas.create_text(90, 180, text='CHIRIQUÍ'),
                                  canvas.create_text(265, 230, text='VERAGUAS'),
                                  canvas.create_text(320, 270, text='HERRERA'),
                                  canvas.create_text(370, 320, text='LOS SANTOS'),
                                  canvas.create_text(360, 190, text='COCLÉ'),
                                  canvas.create_text(420, 155, text='PANAMÁ\n OESTE'),
                                  canvas.create_text(360, 125, text='COLÓN'),
                                  canvas.create_text(510, 110, text='PANAMÁ'),
                                  canvas.create_text(700, 260, text='DARIÉN')]

        for i in canvas_text_provincias:
            canvas.itemconfig(i, fill='#6200EE', activefill='#03DAC6', tag='p', font=self.font_st)

    def create_comarcas_text(self, canvas):
        canvas_text_comarcas = [canvas.create_text(195, 175, text='NGÖBE-BUGLÉ'),
                                canvas.create_text(650, 80, text='GUNA YALA'),
                                canvas.create_text(730, 200, text='EMBERÁ')]

        for i in canvas_text_comarcas:
            canvas.itemconfig(i, fill='#3700B3', activefill='#018786', tag='c', font=self.font_st)

    def on_canvas_click(self, event):
        x = event.x
        y = event.y

        # TODO PENSA MEJOR ESTO
        e = self.display_var.get()
        r = ""
        # provincia
        if e == 2 or e == 0:
            if (30 <= x <= 120) and (80 <= y <= 120):
                r = "Bocas del Toro"
            elif (40 <= x <= 135) and (165 <= y <= 185):
                r = "Chiriquí"
            elif (220 <= x <= 305) and (220 <= y <= 240):
                r = "Veraguas"
            elif (275 <= x <= 360) and (260 <= y <= 280):
                r = "Herrera"
            elif (315 <= x <= 425) and (310 <= y <= 330):
                r = "Los Santos"
            elif (325 <= x <= 390) and (180 <= y <= 200):
                r = "Coclé"
            elif (330 <= x <= 390) and (115 <= y <= 135):
                r = "Colón"
            elif (390 <= x <= 450) and (135 <= y <= 175):
                r = "Panamá Oeste"
            elif (475 <= x <= 550) and (100 <= y <= 120):
                r = "Panamá"
            elif (665 <= x <= 730) and (250 <= y <= 270):
                r = "Darién"

        # comarca
        if e == 1 or e == 0:
            if (135 <= x <= 255) and (165 <= y <= 185):
                r = "Ngöbe-Buglé"
            elif (590 <= x <= 705) and (70 <= y <= 90):
                r = "Guna Yala"
            elif (695 <= x <= 765) and (190 <= y <= 210):
                r = "Emberá"

        if r != "":
            region = get_region(r)
            self.show_sub_window(region)

    # sub windows
    def show_sub_window(self, obj):
        self.frame.destroy()
        # self.configure(background='#FFFFFF')
        self.geometry("800x400")
        self.frame = LabelFrame(self, borderwidth=0, highlightthickness=0, bg=c_white)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)

        obj_tipo = pt.get_o_tipo(obj)

        Button(self.frame, text="\u21E6 ATRAS", bg=c_p2_m, fg=c_black,
               command=lambda: self.show_main_window() if obj_tipo == "r" else self.show_sub_window(region_selec))\
            .grid(row=0, column=0, sticky=W)

        # Titulos
        Label(self.frame, text="USTED SELECCIONO:", font=self.font_t).grid(row=0, column=2, sticky=W)
        Label(self.frame, text=obj.get_nombre(), font=self.font_st).grid(row=0, column=3, sticky=W)

        # Imagen
        Label(self.frame, text="Foto: ", font=self.font_st).grid(row=1, column=0, sticky=W)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = ""

        if obj_tipo == "r":
            global region_selec
            region_selec = obj
            img_path = str(dir_path) + '/img/mapas/' + str(obj.get_nombre()) + '.png'
        elif obj_tipo == "z":
            global zona_selec
            zona_selec = obj
            # TODO ZONA IMG PATH
            img_path = str(dir_path) + '/img/zonas/Bocas del Toro/1.png'

        img = ImageTk.PhotoImage(Image.open(img_path))

        canvas = Canvas(self.frame, height=250, width=250)
        canvas.image = img
        canvas.create_image(125, 125, image=img)
        canvas.grid(row=2, column=0, rowspan=4, columnspan=4, sticky=W)

        # Desc
        Label(self.frame, text="Descripcion:", font=self.font_st).grid(row=1, column=3, sticky=W)
        Label(self.frame, text=obj.get_desc(), justify=LEFT, font=self.font_b, wraplength=245)\
            .grid(row=2, column=3, rowspan=4, sticky=NW)

        # Zonas / Precios
        if obj_tipo == "r":
            Label(self.frame, text="Zonas Turisticas:", font=self.font_st).grid(row=1, column=4, sticky=W)
            zonas = obj.get_zonas()
            for i in range(len(zonas)):
                z = zonas[i]
                Button(self.frame, text=z.get_nombre(), bg=c_p1_v, fg=c_white,
                       command=lambda j=z: self.show_sub_window(j), height=3, width=30)\
                    .grid(row=i + 2, column=4, sticky=W)
        elif obj_tipo == "z":
            Label(self.frame, text="Incluye:", font=self.font_st).grid(row=1, column=4, sticky=W)
            Label(self.frame, text=obj.get_extras(), justify=LEFT, font=self.font_b, wraplength=250) \
                .grid(row=2, column=4, rowspan=4, sticky=NW)
            Label(self.frame, text="Precio: $" + str(obj.get_precio()), font=self.font_st).grid(row=3, column=4, sticky=W)
            Button(self.frame, text="RESERVAR", bg=c_p2_m, fg=c_black, command=self.show_reservar_window)\
                .grid(row=6, column=4, sticky=E)

    def show_reservar_window(self):
        self.frame.destroy()
        # self.configure(background='#FFFFFF')
        self.geometry("800x400")
        self.frame = LabelFrame(self, borderwidth=0, highlightthickness=0, bg=c_white)
        self.frame.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=25, pady=25)

        frame_t = LabelFrame(self.frame, bg=c_white)
        frame_t.place(x=15, y=50)
        frame_e = LabelFrame(self.frame, bg=c_white)
        frame_e.place(x=300, y=50)
        # Titulos
        Label(self.frame, text="RESERVAR", font=self.font_t).pack()
        Button(self.frame, text="\u21E6 ATRAS", bg=c_p2_m, fg=c_black,
               command=lambda: self.show_sub_window(zona_selec)) \
            .place(x=5, y=5)

        Label(frame_t, text="USTED SELECCIONO:", font=self.font_st).grid(row=1, column=0, sticky=W)

        Label(frame_t, text=str(region_selec.get_tipo_nombre()) + " de " + str(region_selec.get_nombre()),
              font=self.font_b).grid(row=2, column=0, sticky=W)
        Label(frame_t, text="Zona: " + str(zona_selec.get_nombre()), font=self.font_b).grid(row=3, column=0, sticky=W)
        Label(frame_t, text="Precio: $" + str(zona_selec.get_precio()) + " por persona",
              font=self.font_b).grid(row=4, column=0, sticky=W)

        Label(frame_t, text="Incluye:", font=self.font_b).grid(row=5, column=0, sticky=W)
        Label(frame_t, text=zona_selec.get_extras(), justify=LEFT, font=self.font_b, wraplength=250) \
            .grid(row=6, column=0, sticky=NW)

        Label(frame_e, text="INFORMACION DEL CLIENTE:", font=self.font_st).grid(row=1, column=1, columnspan=4)

        Label(frame_e, text="Nombre:", font=self.font_b).grid(row=2, column=1)
        nombre = Entry(frame_e)
        nombre.grid(row=2, column=2)

        Label(frame_e, text="Edad:", font=self.font_b).grid(row=2, column=3)
        edad = Entry(frame_e)
        edad.grid(row=2, column=4)

        Label(frame_e, text="Nacionalidad:", font=self.font_b).grid(row=3, column=1)
        nacionalidad = Entry(frame_e)
        nacionalidad.grid(row=3, column=2)

        Label(frame_e, text="Sexo:", font=self.font_b).grid(row=3, column=3)
        sexo = Entry(frame_e)
        sexo.grid(row=3, column=4)

        Label(frame_e, text="Cedula:", font=self.font_b).grid(row=4, column=1)
        sexo = Entry(frame_e)
        sexo.grid(row=4, column=2)

        Label(frame_e, text="Telefono:", font=self.font_b).grid(row=4, column=3)
        telefono = Entry(frame_e)
        telefono.grid(row=4, column=4)

        Label(frame_e, text="Personas:", font=self.font_b).grid(row=5, column=1)
        cnt = Entry(frame_e)
        cnt.grid(row=5, column=2)

        frame_b = LabelFrame(self.frame, bg=c_white)
        frame_b.place(x=500, y=300)
        # Botones
        Button(frame_b, text="CANCELAR", bg=c_p1_v, fg=c_white,
               command=lambda: self.show_main_window(), height=2, width=10)\
            .grid(row=0, column=0)
        Button(frame_b, text="ABONAR", bg=c_p1_v, fg=c_white,
               command=lambda: print("XX"), height=2, width=10)\
            .grid(row=0, column=1)
        Button(frame_b, text="PAGAR", bg=c_p1_v, fg=c_white,
               command=lambda: print("XX"), height=2, width=10)\
            .grid(row=0, column=2)


# Globals
Regiones = pt.get_regiones_list()

region_selec = Region
zona_selec = Zona

# Colores
c_black = '#000000'
c_white = '#FFFFFF'
c_p1_m = '#6200EE'
c_p1_v = '#3700B3'
c_p2_m = '#03DAC6'
c_p2_v = '#018786'
c_error = '#B00020'


def get_region(region):
    if region == "":
        return None

    for i in Regiones:
        if i.get_nombre() == region:
            return i
