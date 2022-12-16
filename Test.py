import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: 2*(x**3) + (x**2) - (13*x) + 6
dx =lambda x: 6*(x**2) + (2*x) - 13
xi = 2.5

i = 1
tolerancia = 0.00001
error = 1
strResult = ""
while error > tolerancia:    
    Raiz = xi - (fx(xi)/dx(xi))
    error = np.abs((Raiz - xi) / Raiz)
    strResult += "n" + str(i) + "\txi=" + str(round(xi,4)) + "\tf(xi)=" + str(round(fx(xi),4)) + "\tf'(xi)=" + str(round(dx(xi),4)) + "\txi+1=" + str(round(Raiz,4)) + "\tError="+str(round(error,6))+"\n"
    xi = Raiz
    i+= 1
print(strResult)
