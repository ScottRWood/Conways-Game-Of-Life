import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from main_2d import init_matrix, update_matrix

LARGE_FONT = ("Verdana", 12)

class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Conway's Game of Life")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        frame = TwoDConway(container, self)
        self.frames[TwoDConway] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(TwoDConway)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class TwoDConway(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="2D Conway's Game of Life", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        x_max = 100
        y_max = 100
        p = 0.5

        self.matrix = init_matrix(x_max, y_max, p)

        self.cmap = colors.ListedColormap(['green', 'white'])
        self.bounds = [0,0.5,1]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

        self.f = Figure(figsize=(5,5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.imshow(self.matrix, cmap=self.cmap, norm=self.norm)

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.update()


    def update(self):
        self.a.clear()

        update_matrix(self.matrix)
        self.a.imshow(self.matrix, cmap=self.cmap, norm=self.norm)

        self.canvas.draw()

        self.after(10, self.update)




app = Window()
app.mainloop()


