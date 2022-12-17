from tkinter import messagebox as mb
import tkinter as tk
from tkinter import ttk
import Views.BiseccionView
import Views.MinimosCuadradosView
import Views.NewtonRaphsonView
import Views.GaussSeidelView
import Views.LagrangeView

window = tk.Tk()
window.title("Metodos Numericos")

#TABS
tabControl = ttk.Notebook(window)
tabs = {
    "Biseccion":None, 
    "Minimos Cuadrados":None, 
    "Newton Raphson":None, 
    "Gauss Seidel":None, 
    "Lagrange":None
    }
for tabName in tabs:
    tab = tk.Frame(tabControl)
    tabControl.add(tab, text = tabName)
    tabs[tabName] = tab
tabControl.grid(row = 0, column=0, sticky="news", padx=5, pady=5)

#Biseccion############################################################
Views.BiseccionView.View(tabs["Biseccion"])
Views.MinimosCuadradosView.View(tabs["Minimos Cuadrados"])
Views.NewtonRaphsonView.View(tabs["Newton Raphson"])
Views.GaussSeidelView.View(tabs["Gauss Seidel"])
Views.LagrangeView.View(tabs["Lagrange"])

######################################################################

####################
#Tablas

#TABLA X2 ###############################


#btnGenerate.bind('<Button-1>', generateNumbers)
#btnLoad.bind('<Button-1>', load)

window.mainloop()