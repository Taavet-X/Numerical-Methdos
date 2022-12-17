from pytexit import py2tex #pip install pytexit
import matplotlib.pyplot as plt
import numpy as np

def buildL(k, X):
    strNumerator = ""
    strDenominator = ""
    for i in range(len(X)):
        if k != i:                                   
            strNumerator += "(x-"+str(X[i])+")*"
            strDenominator += "("+str(X[k])+"-"+str(X[i])+")*"
    return "("+strNumerator[:-1]+")/("+strDenominator[:-1]+")"

def buildP(X, Y):
    p = ""
    for i in range(len(X)):
        p += str(Y[i]) + "*(" + buildL(i, X) + ")+"
    return p[:-1]

def evaluate(x, p):
    return eval(p.replace("x", str(x)))

def ejecutarMetodo(X, Y):
    p = buildP(X, Y)
    #print(evaluate(3, buildP(X, Y)))
    print(p)
    return X, Y, p
    #graficar(X,Y,p)

###################################################

def graficar(X, Y, p):
    latexValue = "$P(x)=" + py2tex(p, print_formula = False)[2:-2] + "$"

    def function(x):
        return eval(p)

    for i in range(len (X)):
        plt.plot(X[i], Y[i], color='red', marker='o', markersize=7)
        
    x = np.linspace(min(X), max(X), 250)
    plt.plot(x, function(x), label=latexValue)
    plt.legend()
    #plt.xlim(a, b)
    plt.show()

#ejecutarMetodo([2.0, 2.5, 4.0], [0.5, 0.4, 0.25])