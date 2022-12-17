import numpy

def ejecutarMetodo(matrix, b, tolerancia, iteracion):
    print(matrix)
    print(b)
    #m=int(input('Valor de m:')) #filas
    #n=int(input('Valor de n:')) #Columnas
    #matrix = numpy.zeros((m,n))
    
    m = len(matrix)
    n = len(matrix[0])

    x=numpy.zeros((m))
    matrix = numpy.matrix(matrix)
    #x = numpy.array(b)

    #vector=numpy.zeros((n)) #Crear un vector que tenga la dimension n
    vector=numpy.array(b) #Crear un vector que tenga la dimension n
    comp=numpy.zeros((m))
    error=[]  #Se declara como una lista 

    '''
    print ('Método de Gauss-Seidel')
    print ('Introduce la matriz de coeficientes y el vector solución')
    for r in range(0,m):
        for c in range(0,n):
            matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
        vector[(r)]=float(input('b['+str(r+1)+']: '))
    print ("Método de Gauss-Seidel")

    tolerancia=float(input("¿Cual es la tolerancia que deseas tener? "))
    iteracion=int(input("¿Cual es el numero maximo de iteraciones? ")) 
    '''
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
    #print(strResult)
    return strResult



