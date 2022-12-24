
'''
Autor:
Nicolás Felipe Victoria Rodríguez - 1767315
'''

import numpy as np
import matplotlib.pyplot as plt
from InputHandler import *

import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
transformations = (standard_transformations + (implicit_multiplication_application,))

def ejecutarMetodo(fx, xi, tolerancia):
    #Llamados para conversion de texto a funcion
    results = []
    t1 = setUpInput(fx)
    fx = lambda x: eval(t1)
    #t2 = setUpInput(dx)    
    #dx = lambda x: eval(t2)

    def dx(x):
        s = sp.Symbol('x') 
        y = parse_expr(t1, transformations=transformations)
        y = y.diff(s)
        return eval(str(y))

    strResult = ""

    i = 0    
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
        strResult += 'n{:<1}: x{:<2}={:.7f}, f(x{:<1})={:.7f}, f\'(x{:<1})={:.7f}'.format(i,i,xiVal,i,fxVal,i,dxVal) + ' error:{}'.format(errorVal) + "\n"
        #strResult += "n" + str(i) + "\txi=" + str(xiVal) + "\tf(xi)=" + str(fxVal) + "\tf'(xi)=" + str(dxVal) + "\txi+1=" + str(raizVal) + "\tError="+str(errorVal)+"\n"
        xi = Raiz
        i+= 1
    strResult += "x = " + str(Raiz)
    return strResult, fx, dx, Raiz, results

