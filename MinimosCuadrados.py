#Puntos
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Ingreso
def ejecutarMetodo(xi, yi):

    #Prodecimiento
    xi = np.array(xi)
    yi = np.array(yi)
    n = len(xi)

    xm = np.mean(xi)
    ym = np.mean(yi)
    sx = np.sum(xi)
    sy = np.sum(yi)
    sxy = np.sum(xi*yi)
    sx2 = np.sum(xi**2)
    sy2 = np.sum(yi**2)

    # Coeficientes 
    a1 = (n*sxy-sx*sy)/(n*sx2-sx**2)
    a0 = ym - a1*xm


    # Polinomio grado 1
    x = sym.Symbol('x')
    f = a0 + a1*x

    fx = sym.lambdify(x,f)
    fi = fx(xi)

    # Coeficiente de correlacion
    numerador = n*sxy-sx*sy
    raiz1 = np.sqrt(n*sx2-sx**2)
    raiz2 = np.sqrt(n*sy2-sy**2)
    r = numerador/(raiz1*raiz2)

    # coeficiente de determinacion
    r2 = r**2
    r2_porcentaje = np.round(r2*100,2)

    #Salida
    strResult = ""
    strResult += 'ymedia = ' + str(ym) +"\n"
    strResult += 'f = '+ str(f) + "\n"
    strResult += 'coeficiente correlacion r = ' + str(r) + "\n"
    strResult += 'coeficiente determinacion r2 = ' + str(r2) + "\n"
    strResult +=  str(r2_porcentaje) +'% de los datos'
    return strResult, xi, yi, fi, n, f


def graficar(xi, yi, fi, n, f):
    # Error
    for i in range(0,n,1):
        y0 = np.min([yi[i],fi[i]])
        y1 = np.max([yi[i],fi[i]])
        plt.vlines(xi[i],y0,y1, color='red',linestyles='dotted')

    #Grafica
    plt.plot(xi,yi,'o',label='(xi,yi)')
    #plt.stem(xi,yi, bottom=ym)
    plt.plot(xi,fi, color='orange', label=f)
    plt.xlabel('xi')
    plt.ylabel('yi')
    plt.legend()
    plt.title('Minimos Cuadrados')
    plt.show()

'''
X = [1,2,3,4,5,6,7]
Y = [0.5,2.5,2,4,3.5,6,5.5]
strResult, xi, yi, fi, n, f = ejecutarMetodo(X, Y)
print(strResult)
graficar(xi, yi, fi, n, f)
'''