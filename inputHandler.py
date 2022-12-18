
'''
Autor:
Germán David Estrada Holguin - 2013122
Manuel Alejandro Perdomo Londoño - 2067575
'''

import numpy as np

pi = 3.141592653589793
e  = 2.718281828459045

def sqrt(x):
    return x**(1/2)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def cot(x):
    return (1/np.tan(x))

def sec(x):
    return (1/np.cos(x))

def csc(x):
    return (1/np.sin(x))
    
#Funciones trigonometricas inversas
def arcsin(x):
    return np.arcsin(x)

def arccos(x):
    return np.arccos(x)

def arctan(x):
    return np.arctain(x)

def arcsec(x):
    return (1/np.arccos(x))

def arcsc(x):
    return (1/np.arcsin(x))

#Funciones hiperbolicas
def sinh(x):
    return np.sinh(x)

def cosh(x):
    return np.cosh(x)

def tanh(x):
    return np.tanh(x)

def coth(x):
    return 1/np.tanh(x)

def sech(x):
    return 1/np.cosh(x)

def csch(x):
    return 1/np.sinh(x)

#Funciones logaritmicas
def ln(x):
    return np.log(x)

def log(x):
    return np.log10(x)

def setUpInput(text):
    text = text.replace("^", "**")
    return text