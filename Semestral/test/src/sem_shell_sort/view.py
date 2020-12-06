import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class BaseView:
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

    # Variables & Widget managers
    def has_variable(self, nombre):
        return nombre in self.variables.keys()

    def add_variable(self, nombre, variable):
        if self.has_variable(nombre):
            raise KeyError("Variable ya existe en el view: {}".format(nombre))
        self.variables[nombre] = variable
        return variable

    def get_variable(self, nombre):
        if not self.has_variable(nombre):
            raise KeyError("Variable no existe en el view: {}".format(nombre))
        return self.variables[nombre]

    def remove_variable(self, nombre):
        if not self.has_variable(nombre):
            raise KeyError("Variable no existe en el view: {}".format(nombre))
        self.variables.pop(nombre)
        return not self.has_variable(nombre)

    def has_widget(self, nombre):
        return nombre in self.widgets.keys()

    def add_widget(self, nombre, widget):
        if self.has_widget(nombre):
            raise KeyError("Variable ya existe en el view: {}".format(nombre))
        self.widgets[nombre] = widget
        return widget

    def get_widget(self, nombre):
        if not self.has_widget(nombre):
            raise KeyError("Variable no existe en el view: {}".format(nombre))
        return self.widgets[nombre]

    def remove_widget(self, nombre):
        if not self.has_widget(nombre):
            raise KeyError("Variable no existe en el view: {}".format(nombre))
        self.widgets.pop(nombre)
        return not self.has_widget(nombre)


class MainView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.show_presentacion_window()

    def show_presentacion_window(self):
        frame = ttk.Frame(self.parent)
        frame.pack_propagate(False)
        frame.pack(expand=tk.TRUE, fill=tk.BOTH, padx=25, pady=25)

        style = ttk.Style()
        style.configure('M.TLabel', font="ubuntu 12")

        ttk.Label(frame, text="UNIVERSIDAD TECNOLÓGICA DE PANAMÁ").pack()
        ttk.Label(frame, text="FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES").pack()
        ttk.Label(frame, text="DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS").pack()
        ttk.Label(frame, text="CARRERA LICENCIATURA EN INGENIERÍA DE SOFTWARE").pack()
        ttk.Label(frame, text="INTRODUCCIÓN A LA TEORÍA COMPUTACIONAL").pack()

        ttk.Label(frame, text="ROYECTO SEMESTRAL").pack(pady=25)

        ttk.Label(frame, text="INTEGRANTES:").pack(pady=5)
        ttk.Label(frame, text="Kevin Feng - 3-748-410").pack()
        ttk.Label(frame, text="Angel Iglesias - 8-958-1").pack()
        ttk.Label(frame, text="Sahori Raby - 8-964-644").pack()
        ttk.Label(frame, text="Luis Villalaz - 8-925-2287").pack()
        ttk.Label(frame, text="Wyming Zeng - 8-966-1043").pack()

        ttk.Label(frame, text="").pack(pady=10)

        ttk.Label(frame, text="Profesor:").pack(pady=5)
        ttk.Label(frame, text="Ing. Samuel Jiménez").pack()

        ttk.Label(frame, text="SEMESTRE II, 2020").pack(pady=25)

        labels = frame.winfo_children()
        for i in labels:
            i.configure(style='M.TLabel')

        ttk.Button(frame, text="EMPEZAR", command=self.load).pack(pady=10)

        self.add_widget("presentacion", frame)

    def load(self):
        self.get_widget("presentacion").destroy()
        self.remove_widget("presentacion")

        main_frame = ttk.Frame(self.parent)
        main_frame.pack_propagate(False)
        main_frame.pack(expand=tk.TRUE, fill=tk.BOTH, padx=50, pady=25)

        self.add_widget("main_frame", main_frame)

        # title Frame
        title_frame = ttk.Frame(main_frame)
        title_frame.pack()

        ttk.Label(title_frame, text="Shell Sorting", font="ubuntu 20").pack(pady=5)

        # button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(anchor=tk.W)

        ttk.Button(button_frame, text="START", width=6, command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        # ttk.Button(button_frame, text="PAUSE/CONTINUE").pack(side=tk.LEFT, padx=5)
        # ttk.Button(button_frame, text="STOP", width=5).pack(side=tk.LEFT, padx=5)

        # self.add_widget("button_frame", button_frame)

        # display Frame
        display_frame = ttk.Frame(main_frame, width=900, height=200)
        display_frame.pack_propagate(False)
        display_frame.pack()

        self.add_widget("display_frame", display_frame)

        # action Frame
        action_frame = ttk.LabelFrame(main_frame, width=900, height=250)
        action_frame.pack_propagate(False)
        action_frame.pack()

        self.add_widget("action_frame", action_frame)

        self.controller.load()

    def start_sorting(self):
        self.controller.start_sorting()


class DisplayView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        canvas = tk.Canvas(self.parent, width=900)
        canvas.configure(bg='black')
        canvas.pack()

        self.add_widget("display_canvas", canvas)

        self.parent.update()
        self.draw_list()

    def draw_list(self):
        canvas = self.get_widget("display_canvas")
        canvas.delete("all")

        self.widgets.clear()
        canvas = self.add_widget("display_canvas", canvas)

        self.add_widget("line", canvas.create_line(0, 0, 0, 0, fill='pink', width=5))

        ilist = self.controller.get_ilist()

        x0 = 450
        list_size = len(ilist)

        if (list_size % 2) == 0:
            s = (list_size / 2) - 1
            x0 -= ((s * 70) + 35)
        else:
            if list_size > 1:
                s = (list_size - 1) / 2
                x0 -= (s * 70)

        for i in range(list_size):

            self.add_widget("square_" + str(i), canvas.create_rectangle(x0 - 25, 75, x0 + 25, 125, fill='blue',
                                                                        outline='white'))
            self.add_widget("text_" + str(i), canvas.create_text((x0, 100), fill='white', text=ilist[i],
                                                                 font=Font(family='ubuntu', size=15, weight='bold')))
            x0 += 70

    def fill_squares(self, id_left, id_right, fill):
        canvas = self.get_widget("display_canvas")

        canvas.itemconfig(self.get_widget("square_" + str(id_left)), fill=fill)
        canvas.itemconfig(self.get_widget("square_" + str(id_right)), fill=fill)

    def draw_connect_line(self, id_left, id_right):
        canvas = self.get_widget("display_canvas")

        x1 = canvas.coords(self.get_widget("square_" + str(id_left)))[0] + 25
        x2 = canvas.coords(self.get_widget("square_" + str(id_right)))[0] + 25

        canvas.coords(self.get_widget("line"), x1, 75, x1, 50, x2, 50, x2, 75)

    def config_text(self, id_left, id_right):
        canvas = self.get_widget("display_canvas")

        work_list = self.controller.get_work_list()

        canvas.itemconfig(self.get_widget("text_" + str(id_left)), text=work_list[id_left])
        canvas.itemconfig(self.get_widget("text_" + str(id_right)), text=work_list[id_right])

    def draw_comparing(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'orange')
        self.draw_connect_line(id_left, id_right)

    def draw_compare_ok(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'green')

    def draw_compare_done(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'blue')

    def draw_compare_found(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'red')

    def draw_found_swap(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'orange')

    def draw_found_ok(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'green')
        self.config_text(id_left, id_right)

    def draw_found_reduce(self, id_left, id_right):
        self.fill_squares(id_left, id_right, 'blue')

    def draw_sorted(self):
        self.get_widget("display_canvas").coords(self.get_widget("line"), 0, 0, 0, 0)


class ActionView(BaseView):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.load()

    def load(self):
        # info frame
        # info_frame = ttk.Frame(self.parent, width=400, height=200)
        # info_frame.pack_propagate(False)
        # info_frame.pack(side=tk.LEFT)

        # self.add_widget("info_frame", info_frame)

        # action canvas frame
        action_canvas_frame = ttk.Frame(self.parent)
        action_canvas_frame.pack(expand=tk.TRUE, fill=tk.BOTH)

        # self.add_widget("action_canvas_frame", canvas_frame)

        canvas = tk.Canvas(action_canvas_frame, width=400, height=200)
        canvas.configure(bg='black')
        canvas.pack()

        self.add_widget("action_canvas", canvas)

        self.add_widget("square_1", canvas.create_rectangle(50, 50, 150, 150, fill='black', outline='black'))
        self.add_widget("square_2", canvas.create_rectangle(250, 50, 350, 150, fill='black', outline='black'))

        self.add_widget("text_1", canvas.create_text((100, 100), fill='white', text='',
                                                     font=Font(family='ubuntu', size=25, weight='bold')))
        self.add_widget("text_2", canvas.create_text((300, 100), fill='white', text='',
                                                     font=Font(family='ubuntu', size=25, weight='bold')))
        self.add_widget("text_3", canvas.create_text((200, 100), fill='white', text='',
                                                     font=Font(family='ubuntu', size=60, weight='bold')))

    def fill_squares(self, fill):
        canvas = self.get_widget("action_canvas")

        canvas.itemconfig(self.get_widget("square_1"), fill=fill)
        canvas.itemconfig(self.get_widget("square_2"), fill=fill, outline='white')

    def outline_squares(self, outline):
        canvas = self.get_widget("action_canvas")

        canvas.itemconfig(self.get_widget("square_1"), outline=outline)
        canvas.itemconfig(self.get_widget("square_2"), outline=outline)

    def config_square_texts(self, id_left, id_right):
        canvas = self.get_widget("action_canvas")

        work_list = self.controller.get_work_list()

        canvas.itemconfig(self.get_widget("text_1"), text=work_list[id_left])
        canvas.itemconfig(self.get_widget("text_2"), text=work_list[id_right])

    def config_symbol_text(self, text):
        self.get_widget("action_canvas").itemconfig(self.get_widget("text_3"), text=text)

    def clear_texts(self):
        canvas = self.get_widget("action_canvas")

        canvas.itemconfig(self.get_widget("text_1"), text="")
        canvas.itemconfig(self.get_widget("text_2"), text="")
        canvas.itemconfig(self.get_widget("text_3"), text="")

    def animate_squares(self):
        canvas = self.get_widget("action_canvas")

        for i in range(10):
            canvas.move(self.get_widget("square_1"), 20, 0)
            canvas.move(self.get_widget("text_1"), 20, 0)

            canvas.move(self.get_widget("square_2"), -20, 0)
            canvas.move(self.get_widget("text_2"), -20, 0)
            canvas.after(50)
            self.parent.update()

    def return_squares(self):
        canvas = self.get_widget("action_canvas")

        canvas.move(self.get_widget("square_1"), -200, 0)
        canvas.move(self.get_widget("text_1"), -200, 0)

        canvas.move(self.get_widget("square_2"), 200, 0)
        canvas.move(self.get_widget("text_2"), 200, 0)

    def wait(self):
        self.parent.update()
        self.parent.after(500)

    def draw_comparing(self, id_left, id_right):
        self.fill_squares('orange')
        self.outline_squares('white')
        self.config_square_texts(id_left, id_right)
        self.wait()

    def draw_compare_ok(self):
        self.fill_squares('green')
        self.config_symbol_text("<")
        self.wait()

    def draw_compare_done(self):
        self.config_symbol_text("")
        # update out?
        self.parent.update()

    def draw_compare_found(self):
        self.fill_squares('red')
        self.config_symbol_text(">")
        self.wait()

    def draw_found_swap(self):
        self.fill_squares('blue')
        self.config_symbol_text("")
        self.animate_squares()

    def draw_found_ok(self, id_left, id_right):
        self.return_squares()

        self.fill_squares('green')
        self.config_square_texts(id_left, id_right)
        self.config_symbol_text("<")

        self.wait()

    def draw_found_reduce(self):
        self.config_symbol_text("")
        # update out?
        self.parent.update()

    def draw_sorted(self):
        self.fill_squares('black')
        self.outline_squares('black')
        self.clear_texts()

        self.parent.update()
