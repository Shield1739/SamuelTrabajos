from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from os import path

colores_codigos = [
    "blue", "green", "yellow",
    "red", "deep pink", "purple"
]

colores_nombres = [
    "Azul", "Verde", "Amarillo",
    "Rojo", "Rosado", "Purpura"
]


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Laboratorio #4 - Programa 2")
        self.geometry("375x400")
        self.resizable(False, False)

        self.frame = LabelFrame()

        self.input_var = StringVar()
        self.input = Entry()

        self.canvas = Canvas(self, height=300, width=300)
        self.valid = False

    # frames
    def create_new_frame(self):
        self.frame.destroy()
        self.frame = LabelFrame(self, padx=10, pady=0, borderwidth=0, highlightthickness=0)
        self.frame.pack(padx=10, pady=40)

    def show_main_window(self):
        self.create_new_frame()

        for i in range(2):
            for j in range(3):
                cod = colores_codigos[(i * 3) + j]
                Button(self.frame, text=colores_nombres[(i * 3) + j], command=lambda e=cod: self.button_pressed(e),
                       height=2, width=9, bg=cod).grid(row=i, column=j)

        Button(self.frame, text="BORRAR", command=lambda: self.borrar_img(),
               height=2, width=9).grid(row=1, column=3)

    def button_pressed(self, e):
        # print(path.join(path.dirname(__file__), "colores.py"))
        if self.valid:
            show_errorbox("Debe borrar la imagen antes de abrir otra")
            return

        self.valid = True

        img = ImageTk.PhotoImage(Image.open('colores/img/' + str(e) + '.jpg'))

        self.canvas.image = img
        self.canvas.create_image(100, 100, image=img)
        self.canvas.pack()

    def borrar_img(self):
        self.canvas.destroy()
        self.canvas = Canvas(self, height=300, width=300)
        self.valid = False


def show_errorbox(msg):
    messagebox.showerror("error", msg)


app = App()
app.show_main_window()
app.mainloop()
