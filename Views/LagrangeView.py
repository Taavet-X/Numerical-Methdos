
'''
Autor:
Germán David Estrada Holguin - 2013122
'''

import tkinter as tk
import numpy as np
import matplotlib
import Lagrange
from pytexit import py2tex #pip install pytexit

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

        lblX = tk.Label(master = frmOptions, text = "X = ")
        lblX.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entX = entX = tk.Entry(master = frmOptions)
        entX.grid(row = 0, column = 1, columnspan = 1, sticky = "news", padx = 5, pady = 5)
        entX.insert(0, "2.0, 2.5, 4.0")

        lblY = tk.Label(master = frmOptions, text = "Y = ")
        lblY.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entY = entY = tk.Entry(master = frmOptions)
        entY.grid(row = 1, column = 1, sticky = "news", padx = 5, pady = 5)
        entY.insert(0, "0.5, 0.4, 0.25")

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
        self.axes.set_title('Minimos Cuadrados')

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.textOutput = txtOutput = tk.Text(master, height=10)
        #txtOutput.grid(column=1, row=0, rowspan=2, sticky="news")
        txtOutput.grid(column=0, row=2, sticky="news")        
        master.grid_rowconfigure(2, weight = 1)
    
    def execute(self, event):
        X = self.entX.get().split(",")
        Y = self.entY.get().split(",")
        for i in range(len(X)):
            X[i] = float(X[i])
            Y[i] = float(Y[i])
        #X = [1,2,3,4,5,6,7]
        #Y = [0.5,2.5,2,4,3.5,6,5.5]
        X, Y, strResult = Lagrange.ejecutarMetodo(X, Y)
        self.textOutput.delete('1.0', tk.END)
        self.textOutput.insert(tk.END, strResult + "\n") 
        self.graficar(X, Y, strResult)

    def graficar(self,  X, Y, p):

        latexValue = "$P(x)=" + py2tex(p, print_formula = False)[2:-2] + "$"

        def function(x):
            return eval(p)

        for i in range(len (X)):
            self.axes.plot(X[i], Y[i], color='red', marker='o', markersize=7)
            
        x = np.linspace(min(X), max(X), 250)
        self.axes.plot(x, function(x), label=latexValue)
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.legend()
        self.axes.set_title('Lagrange')

        self.figure_canvas.draw()
        self.axes.clear()