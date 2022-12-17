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

#Funciones logaritmicas
def ln(x):
    return np.log(x)

def log(x):
    return np.log10(x)

def setUpInput(text):
    text = text.replace("^", "**")
    #text = text.replace("sin", "np.sin")
    #text = text.replace("cos", "np.cos")
    #text = text.replace("tan", "np.tan")
    #text = text.replace("cot", "1/np.tan")
    #text = text.replace("sec", "1/np.cos")
    #text = text.replace("csc", "1/np.sin")    
    #text = text.replace("ln", "np.log")
    
    #text = text.replace("log", "np.log10")
    return text

#x = 3.14
#print(eval(setUpInput("(1/2)*x^(-1/2)")))