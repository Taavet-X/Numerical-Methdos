
'''
Autor:
Manuel Alejandro Perdomo Londoño - 2067575
'''

import numpy as np
from InputHandler import *

strResult = ""

# Numero de iteraciones teoricas
def iteraciones(a,b,tol=10**-4):
    return np.log((b-a)/tol)/np.log(2)

# Busca de nuevo intervalo
def new_inter(f,a,b,n=5):
    global strResult
    b_t = (a+b)/2
    if a<=b_t and b_t<=b and n>0:
        if f(a)*f(b_t) >= 0:
            n -= 1
            new_inter(f,a,b_t,n)
        else:
            strResult += "f(a) y f(b) No presentan cambio de signo\n"
            strResult += "Se usara el subintervalo [" + str(a) + ", "+str(b_t) + "]\n"
            return a,b_t

# Metodo De Biseccion
def metodo_biseccion(t,a,b,tol=10**-4,n=50):
    global strResult
    strResult = ""
    t = setUpInput(t)
    f = lambda x: eval(t)
    ite_teoricas = iteraciones(a,b, tol)
    a_graf = a
    b_graf = b
    if f(a)*f(b) > 0:  # el intevalo escogido no sirve
        newInter = new_inter(f,a,b)
        if newInter != None:
          a,b = newInter
        else:          
          return "Error: El intervalo no funciona", f, a_graf, b_graf, None 
    
    e_abs = abs(b-a)
    i = 1
    while i <= n and e_abs > tol:
        c = (a + b)/2  # punto medio
        strResult += 'n{:<2}: a{:<2}={:.7f} , b{:<2}={:.7f}, c{:<2}={:.7f}'.format(i,i-1,a,i-1,b,i,c) + ' error:{}'.format(e_abs) + "\n"
        if f(c)==0:  # solución exacta encontrada
            strResult += 'Solución encontrada x={:.7f}'. format(c)
            return strResult, f, a_graf, b_graf, c
        if f(a)*f(c)<0:  # escoger intervalo izquierdo
            b = c
            c_t = a
        else:  # escoger intervalo derecho
            a = c
            c_t = b
        e_abs = abs(c_t - c)  # error absoluto
        if e_abs < tol:  # criterio de parada            
            strResult += 'Solución encontrada x= {:.7f}\nValor de f(c)= {}\niteraciones: {}'. format(c,f(c),i) + '\nIteraciones Teoricas: {}'.format(ite_teoricas)
            return strResult, f, a_graf, b_graf, c
        i += 1    
    strResult += 'Solución no encontrada, iteraciones agotadas: {}'.format(i-1)
    return strResult, f, a_graf, b_graf, None