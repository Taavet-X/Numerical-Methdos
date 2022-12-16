import numpy
m=int(input('Valor de m:')) #filas
n=int(input('Valor de n:')) #Columnas
matrix = numpy.zeros((m,n))
x=numpy.zeros((m))

vector=numpy.zeros((n)) #Crear un vector que tenga la dimension n
comp=numpy.zeros((m))
error=[]  #Se declara como una lista 



print ('Método de Gauss-Seidel')
print ('Introduce la matriz de coeficientes y el vector solución')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
    vector[(r)]=float(input('b['+str(r+1)+']: '))
print ("Método de Gauss-Seidel")

tolerancia=float(input("¿Cual es la tolerancia que deseas tener? "))
iteracion=int(input("¿Cual es el numero maximo de iteraciones? ")) 

#Aca comienza el metodo
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
        print("x[" + str(r)+"]: "+ str(x[r]))
    del error[:]
    #Comprobación
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            suma=suma+matrix[r,c]*x[c]

        comp[r]=suma
        dif=abs(comp[r]-vector[r])
        error.append(dif)
        print("Error en x[", r,"]= ",error[r])
    
    print("Iteraciones ", k)
    if all (i<=tolerancia for i in error) == True:
        break

print("Programa terminado") 



