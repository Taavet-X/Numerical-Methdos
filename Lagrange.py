def buildL(k):
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
        p += str(Y[i]) + "*(" + buildL(i) + ")+"
    return p[:-1]

def evaluate(x, p):
    return eval(p.replace("x", str(x)))

X = [2.0, 2.5, 4.0]
Y = [0.5, 0.4, 0.25]
p = buildP(X, Y)
print(evaluate(3, buildP(X, Y)))
print(p)

###################################################
from pytexit import py2tex #pip install pytexit
latexValue = "$P(x)=" + py2tex(p, print_formula = False)[2:-2] + "$"

import matplotlib.pyplot as plt
import numpy as np

def function(x):
    return eval(p)

for i in range(len (X)):
    plt.plot(X[i], Y[i], color='red', marker='o', markersize=7)
    
x = np.linspace(min(X), max(X), 250)
plt.plot(x, function(x), label=latexValue)
plt.legend()
#plt.xlim(a, b)
plt.show()