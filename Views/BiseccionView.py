import tkinter as tk
import numpy as np
import matplotlib
import Biseccion

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class View:

    def __init__(self, master):
        frmOptions = tk.Frame(master = master, relief=tk.GROOVE, borderwidth=1)
        frmOptions.grid(row = 0, column=0, sticky="news")
        frmOptions.grid_columnconfigure(4, weight = 1)

        lblF = tk.Label(master = frmOptions, text = "f(x) = ")
        lblF.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entF = entF = tk.Entry(master = frmOptions)
        entF.grid(row = 0, column = 1, columnspan = 4, sticky = "news", padx = 5, pady = 5)
        entF.insert(0, "sin(x)")

        lblA = tk.Label(master = frmOptions, text = "a")
        lblA.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entA = entA = tk.Entry(master = frmOptions)
        entA.grid(row = 1, column = 1, sticky = "news", padx = 5, pady = 5)
        entA.insert(0, "3")
        lblB = tk.Label(master = frmOptions, text = "b")
        lblB.grid(row = 1, column = 2, sticky = "news", padx = 5, pady = 5)
        self.entB = entB = tk.Entry(master = frmOptions)
        entB.insert(0, "7")
        entB.grid(row = 1, column = 3, sticky = "news", padx = 5, pady = 5)

        btnExecute = tk.Button(master = frmOptions, text = "Ejecutar")
        btnExecute.grid(row = 1, column = 4, sticky="news", padx = 5, pady = 5)
        btnExecute.bind('<Button-1>', self.execute)

        frmBiseccionGraph = tk.Frame(master = master, relief=tk.GROOVE, borderwidth=1)
        frmBiseccionGraph.grid(row = 1, column=0, sticky="news")
        #frmOptions.grid_columnconfigure(1, weight = 1)

        # create a figure
        self.figure = Figure(figsize=(6, 4), dpi=100)        
        self.figure_canvas = FigureCanvasTkAgg(self.figure, frmBiseccionGraph)
        NavigationToolbar2Tk(self.figure_canvas, frmBiseccionGraph)
        self.axes = self.figure.add_subplot()

        self.axes.set_xlabel('xi')
        self.axes.set_ylabel('yi')
        self.axes.set_title('Biseccion')

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.textOutput = txtOutput = tk.Text(master, height=10)
        #txtOutput.grid(column=1, row=0, rowspan=2, sticky="news")
        txtOutput.grid(column=0, row=2, sticky="news")        
        master.grid_rowconfigure(2, weight = 1)
    
    def execute(self, event):
        f = self.entF.get()
        a = float(self.entA.get())
        b = float(self.entB.get())
        strResult, f, a_graf, b_graf, c = Biseccion.metodo_biseccion(f,a,b)
        self.textOutput.delete('1.0', tk.END)
        self.textOutput.insert(tk.END, strResult + "\n") 
        self.graficar(f, a_graf, b_graf, c)

    def graficar(self, f, x_i, x_f, c=0, num = 1000):
        x = np.linspace(x_i, x_f, num)
        #fig, ax = plt.subplots(figsize=(15,5))
        self.axes.plot(x, f(x))
        xmin, xmax = self.axes.get_xlim()
        ymin, ymax = self.axes.get_ylim()
        self.axes.annotate("", xy=(xmax,0), xytext=(xmin,0), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
        self.axes.annotate("", xy=(0,ymax), xytext=(0,ymin), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
        if(c != 0 and c != None):
            etiqueta = c,f(c)
            self.axes.plot(c, f(c), color='red', marker='o', markersize=7,label=etiqueta)
        self.axes.set_xlabel('xi')
        self.axes.set_ylabel('yi')
        self.axes.legend()
        self.axes.set_title('Biseccion')


        self.figure_canvas.draw()
        self.axes.clear()
        #self.figure.show()