from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Laboratorio #4 - Programa 1")
        self.geometry("375x300")
        self.resizable(False, False)

        self.frame = LabelFrame()

        self.input_var = StringVar()
        self.input = Entry()

    # frames
    def create_new_frame(self):
        self.frame.destroy()
        self.frame = LabelFrame(self, padx=10, pady=0, borderwidth=0, highlightthickness=0)
        self.frame.pack(padx=10, pady=40)

    def show_main_window(self):
        self.create_new_frame()

        self.input = Entry(self.frame, textvariable=self.input_var, state='disabled')
        self.input.grid(row=0, column=0, columnspan=3, ipadx=50, ipady=5)

        count = 7
        for i in range(3):
            for j in range(3):
                Button(self.frame, text=count, command=lambda e=count: self.button_pressed(e),
                       height=2, width=9).grid(row=1+i, column=j)
                count += 1
            count -= 6

        Button(self.frame, text=0, command=lambda: self.button_pressed(0),
               height=2, width=20).grid(row=4, column=0, columnspan=2)
        Button(self.frame, text="CLEAR", command=lambda: self.clear_input(),
               height=2, width=9).grid(row=4, column=2)

        Button(self.frame, text="Binario - Decimal", command=lambda: self.binario_to_decimal(self.input_var.get()),
               height=2).grid(row=1, column=3)
        Button(self.frame, text="Decimal - Binario", command=lambda: self.decimal_to_binario(int(self.input_var.get())),
               height=2).grid(row=2, column=3)

    def button_pressed(self, e):
        self.input_var.set(self.input_var.get() + str(e))

    def clear_input(self):
        self.input_var.set("")

    def decimal_to_binario(self, e):
        self.input_var.set(bin(e).replace("0b", ""))

    def binario_to_decimal(self, e):
        try:
            e = int(e, 2)
        except TypeError:
            show_errorbox("No es un numero decimal")
            return

        self.input_var.set(e)


def show_errorbox(msg):
    messagebox.showerror("error", msg)


app = App()
app.show_main_window()
app.mainloop()
