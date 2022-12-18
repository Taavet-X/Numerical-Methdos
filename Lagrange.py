
'''
Autor:
Germán David Estrada Holguin - 2013122
'''

from pytexit import py2tex #pip install pytexit
import matplotlib.pyplot as plt

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
    return eval(p)

def ejecutarMetodo(X, Y):
    p = buildP(X, Y)
    return X, Y, p