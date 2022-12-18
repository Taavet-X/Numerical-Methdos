
'''
Autor:
Germán David Estrada Holguin - 2013122
'''

import tkinter as tk
import numpy as np
import matplotlib
import GaussSeidel

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

        lblTolerancia = tk.Label(master = frmOptions, text = "Tolerancia = ")
        lblTolerancia.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entTolerancia = entTolerancia = tk.Entry(master = frmOptions)
        entTolerancia.grid(row = 0, column = 1, columnspan = 1, sticky = "news", padx = 5, pady = 5)
        entTolerancia.insert(0, "0.0001")

        lblIteraciones = tk.Label(master = frmOptions, text = "Iteraciones = ")
        lblIteraciones.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 5)
        self.entIteraciones = entIteraciones = tk.Entry(master = frmOptions)
        entIteraciones.grid(row = 1, column = 1, sticky = "news", padx = 5, pady = 5)
        entIteraciones.insert(0, "10")

        btnExecute = tk.Button(master = frmOptions, text = "Ejecutar")
        btnExecute.grid(row = 1, column = 4, sticky="news", padx = 5, pady = 5)
        btnExecute.bind('<Button-1>', self.execute)

        frmBiseccionGraph = tk.Frame(master = master, relief=tk.GROOVE, borderwidth=1)
        frmBiseccionGraph.grid(row = 1, column=0, sticky="news")
        #frmOptions.grid_columnconfigure(1, weight = 1)

        
        self.textInput = textInput = tk.Text(master)
        #txtOutput.grid(column=1, row=0, rowspan=2, sticky="news")
        textInput.grid(column=0, row=2, sticky="news")    
        strInput = "3x1 - 0.1x2 - 0.2x3 = 7.85\n0.1x1 + 7x2 - 0.3x3 = -19.3\n0.3x1 - 0.2x2 + 10x3 = 71.4"
        self.textInput.insert(tk.END, strInput)   


        self.textOutput = txtOutput = tk.Text(master, height=10)
        #txtOutput.grid(column=1, row=0, rowspan=2, sticky="news")
        txtOutput.grid(column=0, row=3, sticky="news")        
        master.grid_rowconfigure(3, weight = 1)
    
    def execute(self, event):
        toleracia = float(self.entTolerancia.get())
        iteraciones = int(self.entIteraciones.get())
        input = self.textInput.get('1.0', tk.END)
        input = input.split("\n")
        b = []
        m = []
        for line in input:
            if len(line) > 0:                
                line = line.split("=")            
                flag = True                
                number = ""
                row = []
                for char in line[0]:
                    if char == "+":
                        if number != "":
                            row.append(float(number))
                        number = "+"                                        
                        flag = True
                    elif char == "-":
                        if number != "":
                            row.append(float(number))
                        number = ""  
                        number = "-"
                        flag = True
                    elif (char.isnumeric() or char == ".") and flag:
                        number += char
                    elif char != " ":
                        flag = False
                row.append(float(number))
                m.append(row)                     
                b.append(float(line[1]))
        strResult = GaussSeidel.ejecutarMetodo(m, b, toleracia, iteraciones)
        self.textOutput.delete('1.0', tk.END)
        self.textOutput.insert(tk.END, strResult + "\n") 