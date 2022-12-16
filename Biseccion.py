import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')
#%matplotlib inline

def graficar(f, x_i, x_f,c=0, num = 1000):
    x = np.linspace(x_i, x_f, num)
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(x, f(x))
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.annotate("", xy=(xmax,0), xytext=(xmin,0), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    ax.annotate("", xy=(0,ymax), xytext=(0,ymin), arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))
    if(c != 0):
        etiqueta = c,f(c)
        plt.plot(c, f(c), color='red', marker='o', markersize=7,label=etiqueta)

    plt.xlabel('xi')
    plt.ylabel('yi')
    plt.legend()
    plt.title('Biseccion')
    plt.show()


#graficar(f1,0.01, 1.6)

# Numero de iteraciones teoricas

def iteraciones(a,b,tol=10**-4):
    print(a,b)
    return np.log((b-a)/tol)/np.log(2)

# Busca de nuevo intervalo
def new_inter(f,a,b,n=5):
    b_t = (a+b)/2
    if a<=b_t and b_t<=b and n>0:
        if f(a)*f(b_t) >= 0:
            n -= 1
            print("iteraciones: ",n)
            new_inter(f,a,b_t,n)
        else:
            print("Puntos: ",a,b_t)  
            return a,b_t


# Metodo De Biseccion

def metodo_biseccion(f,a,b,tol=10**-4,n=50):
    
    ite_teoricas = iteraciones(a,b)
    a_graf = a
    b_graf = b
    if f(a)*f(b) >= 0:  # el intevalo escogido no sirve
        if new_inter(f,a,b) != None:
          a,b = new_inter(f,a,b)
        else:
          print('El intervalo no funciona, f(a)={:.2f} y f(b)={:.2f}'.format(f(a),f(b)))
          return None
    
    e_abs = abs(b-a)
    i = 1
    while i <= n and e_abs > tol:
        c = (a + b)/2  # punto medio
        print('ite {:<2}: a_{:<2}={:.7f} , b_{:<2}={:.7f}, c_{:<2}={:.7f}'.format(i,i-1,a,i-1,b,i,c),'error:{}'.format(e_abs))
        if f(c)==0:  # solución exacta encontrada
            print('Solución encontrada x={:.7f}'. format(c))
            return c
        if f(a)*f(c)<0:  # escoger intervalo izquierdo
            b = c
            c_t = a
        else:  # escoger intervalo derecho
            a = c
            c_t = b
        e_abs = abs(c_t - c)  # error absoluto
        if e_abs < tol:  # criterio de parada
            print('Solución encontrada x= {:.7f},Valor de f(c)= {},iteraciones: {}'. format(c,f(c),i),'Iteraciones Teoricas: {}'.format(ite_teoricas))
            graficar(f,a_graf,b_graf,c)
            return c
        i += 1
    print ('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    return None

#Funciones
def f1(x):
    return x + np.log(x)

def f2(x):
    return np.sin(x)

#graficar(f2,3,7)

# Llamadas al metodo
metodo_biseccion(f2,3,7)