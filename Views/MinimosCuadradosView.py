import tkinter as tk
import numpy as np
import matplotlib
import MinimosCuadrados

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
        entX.insert(0, "1,2,3,4,5,6,7")

        lblY = tk.Label(master = frmOptions, text = "Y")
        lblY.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entY = entY = tk.Entry(master = frmOptions)
        entY.grid(row = 1, column = 1, sticky = "news", padx = 5, pady = 5)
        entY.insert(0, "0.5,2.5,2,4,3.5,6,5.5")

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
        strResult, xi, yi, fi, n, f = MinimosCuadrados.ejecutarMetodo(X, Y)
        self.textOutput.delete('1.0', tk.END)
        self.textOutput.insert(tk.END, strResult + "\n") 
        self.graficar( xi, yi, fi, n, f)

    def graficar(self,  xi, yi, fi, n, f):
        for i in range(0,n,1):
            y0 = np.min([yi[i],fi[i]])
            y1 = np.max([yi[i],fi[i]])
            self.axes.vlines(xi[i],y0,y1, color='red',linestyles='dotted')

        #Grafica
        self.axes.plot(xi,yi,'o',label='(xi,yi)')
        #plt.stem(xi,yi, bottom=ym)
        self.axes.plot(xi,fi, color='orange', label=f)
        self.axes.set_xlabel('xi')
        self.axes.set_ylabel('yi')
        self.axes.legend()
        self.axes.set_title('Minimos Cuadrados')

        self.figure_canvas.draw()
        self.axes.clear()
        '''

        x = np.linspace(x_i, x_f, num)
        #fig, ax = plt.subplots(figsize=(15,5))
        self.axes.plot(x, f(x))
        xmin, xmax = self.axes.get_xlim()
        ymin, ymax = self.axes.get_ylim()
        self.axes.annotate("", xy=(xmax,0), xytext=(xmin,0), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
        self.axes.annotate("", xy=(0,ymax), xytext=(0,ymin), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
        if(c != 0):
            etiqueta = c,f(c)
            self.axes.plot(c, f(c), color='red', marker='o', markersize=7,label=etiqueta)

        self.figure_canvas.draw()
        self.axes.clear()
        #self.figure.show()
        '''