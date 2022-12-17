import numpy as np
import matplotlib.pyplot as plt
from inputHandler import *

def ejecutarMetodo(fx, dx, xi):
    #Llamados para conversion de texto a funcion
    results = []
    t1 = setUpInput(fx)
    fx = lambda x: eval(t1)
    t2 = setUpInput(dx)
    dx = lambda x: eval(t2)
    strResult = ""

    i = 1
    tolerancia =0.00001
    error = 1
    while error > tolerancia:
        if i == 50:
            return "No ha sido posible encontrar la solucion", fx, dx, Raiz, results
        Raiz = xi - (fx(xi)/dx(xi))
        error = np.abs((Raiz - xi) / Raiz)
        
        fxVal = fx(xi)
        dxVal = dx(xi)
        recta = (lambda fx, dx, xi: lambda x: (dx * x) + (fx - (dx* xi)) )(fxVal, dxVal, xi) #Recta tangente al punto xi
        results.append([xi, fxVal, recta])
        #Redondeos para acortar el string
        try:
            xiVal = round(xi,4)
        except:
            xiVal = xi
        try:
            fxVal = round(fxVal,4)
        except:
            pass
        try:
            dxVal = round(dxVal, 4)
        except:
            pass
        try:
            raizVal = round(Raiz, 4)
        except:
            raizVal = Raiz
        try:
            errorVal = round(error,6)
        except:
            errorVal = error
        strResult += "n" + str(i) + "\txi=" + str(xiVal) + "\tf(xi)=" + str(fxVal) + "\tf'(xi)=" + str(dxVal) + "\txi+1=" + str(raizVal) + "\tError="+str(errorVal)+"\n"
        xi = Raiz
        i+= 1
    return strResult, fx, dx, Raiz, results

