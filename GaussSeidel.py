
'''
Autor:
Cristhian Camilo Lozano Gómez - 2067818
'''

import numpy

def ejecutarMetodo(matrix, b, tolerancia, iteracion):
    
    m = len(matrix)
    n = len(matrix[0])

    x=numpy.zeros((m))
    matrix = numpy.matrix(matrix)

    vector=numpy.array(b) #Crear un vector que tenga la dimension n
    comp=numpy.zeros((m))
    error=[]  #Se declara como una lista 

    #Aca comienza el metodo
    strResult = ""
    k=0
    while k < iteracion:
        suma=0
        k=k+1
        for r in range(0,m):
            suma=0
            for c in range(0,n):
                if (c != r):
                    suma=suma+matrix[r,c]*x[c]               
            x[r]=(vector[r]-suma)/matrix[r,r]
            strResult += "x[" + str(r) + "]: " + str(x[r]) + "\n"
        del error[:]
        #Comprobación
        for r in range(0,m):
            suma=0
            for c in range(0,n):
                suma=suma+matrix[r,c]*x[c]

            comp[r]=suma
            dif=abs(comp[r]-vector[r])
            error.append(dif)
            strResult += "Error en x[" + str(r) + "]= " + str(error[r]) + "\n"
        
        strResult += "Iteraciones " + str(k) + "\n"
        if all (i<=tolerancia for i in error) == True:
            break

    return strResult



