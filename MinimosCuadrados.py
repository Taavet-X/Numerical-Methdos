
'''
Autor:
Manuel Alejandro Perdomo Londoño - 2067575
'''

#Puntos
import numpy as np
import sympy as sym

#Ingreso
def ejecutarMetodo(X, Y):

    #Prodecimiento
    X = np.array(X)
    Y = np.array(Y)
    n = len(X)
    mediaX = np.mean(X)
    mediaY = np.mean(Y)
    sumatoriaX = np.sum(X)
    sumatoriaY = np.sum(Y)
    sumatoriaXY = np.sum(X*Y)
    sumatoriaXCuadrado = np.sum(X**2)
    sumatoriaYCuadrado = np.sum(Y**2)

    # Coeficientes 
    a1 = (n*sumatoriaXY-sumatoriaX*sumatoriaY)/(n*sumatoriaXCuadrado-sumatoriaX**2)
    a0 = mediaY - a1*mediaX

    # Polinomio grado 1
    x = sym.Symbol('x')
    f = a0 + a1*x

    fx = sym.lambdify(x,f)
    fi = fx(X)

    # Coeficiente de correlacion    
    raiz1 = np.sqrt(n*sumatoriaXCuadrado-sumatoriaX**2)
    raiz2 = np.sqrt(n*sumatoriaYCuadrado-sumatoriaY**2)
    r = (n*sumatoriaXY-sumatoriaX*sumatoriaY)/(raiz1*raiz2)

    # coeficiente de determinacion
    r2 = r**2
    r2_porcentaje = np.round(r2*100,2)

    #Salida
    strResult = ""
    strResult += 'mediaYedia = ' + str(mediaY) +"\n"
    strResult += 'f = '+ str(f) + "\n"
    strResult += 'coeficiente correlacion r = ' + str(r) + "\n"
    strResult += 'coeficiente determinacion r2 = ' + str(r2) + "\n"
    strResult +=  str(r2_porcentaje) +'% de los datos'
    return strResult, X, Y, fi, n, f