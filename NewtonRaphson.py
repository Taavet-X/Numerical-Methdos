import numpy as np
import matplotlib.pyplot as plt
from inputHandler import setUpInput

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
        Raiz = xi - (fx(xi)/dx(xi))
        error = np.abs((Raiz - xi) / Raiz)
        
        fxVal = fx(xi)
        dxVal = dx(xi)
        recta = (lambda fx, dx, xi: lambda x: (dx * x) + (fx - (dx* xi)) )(fxVal, dxVal, xi) #Recta tangente al punto xi
        results.append([xi, fxVal, recta])
        strResult += "n" + str(i) + "\txi=" + str(round(xi,4)) + "\tf(xi)=" + str(round(fxVal,4)) + "\tf'(xi)=" + str(round(dxVal,4)) + "\txi+1=" + str(round(Raiz,4)) + "\tError="+str(round(error,6))+"\n"
        xi = Raiz
        i+= 1
    return strResult, fx, dx, Raiz, results

