import matplotlib.pyplot as plt 
import numpy as np
import random 
from matplotlib import animation
from copy import copy
#from matplotlib.animation import PillowWriter
from sklearn.linear_model import LinearRegression  
import seaborn as sns
regresion_lineal = LinearRegression() # creamos una instancia de la funcion



#Damos formato de estilo a las gráficas
plt.style.use(['seaborn']) 
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

#Inicialización del sistema
N = 50 #Numero de elementos, debe ser impar
pasos = 250 #Numero de iteraciones
sistema = np.zeros((N,N),dtype=int) #Matriz inicial
num_ite = []
num_cuadros = []
difusion = []#Almacena las posiciones 
#config = []
semilla = int((N-1)/2) #Numero que nos asegura posicionarnos en el centro del arreglo
sistema[semilla,semilla] = 1 #Colocamos la semilla
difusion.append((semilla,semilla)) 

#Indices sobre los que corre la posicion de los pixeles
nx=0
ny=0
k=0
r_list = [] #Distancias que si cumplen el valor del criterio
i=0 #Detener la iteracion 
step=0


while step <= pasos:
    i, j = random.choice(difusion) #Elegimos un pixel con valor 1
    nx = i + random.randint(-1,1) #Nos podemos mover a la izquierda o a la derecha de forma aleatoria
    ny = j + random.randint(-1,1) #Nos podemos mover arriba o abajo de forma aleatoria
    while nx < 0 or nx> N-1 or ny<0 or ny>N-1: #Nos aseguramos de que siempre tengamos 8 vecinos
        nx = i + random.randint(-1,1) 
        ny = j + random.randint(-1,1)
        
    pi,pj = difusion[-1] #Extraemos el ultimo elemento de la lista
    r = np.sqrt((pi-nx)**2 + (pj-ny)**2) #Calculamos la distancia con los indices de la posicion
    criterio = 2.5 #Distancia de corte
    if sistema[nx,ny] == 0 and r<criterio: #Si tenemos un cero y además se cumple la condición 
        sistema[nx,ny]=1                   #cambiamos el 0 por un 1
        r_list.append(r)                   #Guardamos el valor del radio
        #config.append(copy(sistema))
        difusion.append((nx,ny)) #Guardamos las coordenadas
        step +=1 #Contador
    num_cuadros.append(len(difusion)) #Guardamos el número de cuadros por cada evolución temporal
    k+=1 #Contador temporal
    num_ite.append(k) #Guardamos en una lista el contador
 
#Convertimos en arreglos numericos para poder graficar    
x1=np.array(num_ite) 
y1=np.array(num_cuadros)

#Hacemos una regresión lineal para calcular la pendiente de la recta
regresion_lineal.fit(x1.reshape(-1,1), y1) # instruimos a la regresión lineal que aprenda de los datos (x,y)
# vemos los parámetros que ha estimado la regresión lineal
print('w = ' + str(regresion_lineal.coef_) + ', b = ' + str(regresion_lineal.intercept_))

#Graficando la pendiente
def f(m):  # función f(x) = w*x + b + Ruido_Gaussiano
    z = regresion_lineal.coef_*x2 +  regresion_lineal.intercept_
    return z
x2 = np.arange(0, 9000, 1)
y2 = f(x2)
#grafica estado final
plt.figure()
plt.plot(x2,y2,label='data', color='green')
plt.plot(num_ite,num_cuadros,"om",label="Puntos del modelo")
plt.ylabel("Área")
plt.xlabel("Tiempo")
plt.title("Evolución del sistema")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize = (6,6))
plt.title('Difusión, {} iteraciones, r_prom = {:3.2f}'
          . format(pasos,  np.mean(r_list)),
          fontdict = font)

plt.contourf(sistema, cmap = 'plasma')
plt.show()

#fig, ax = plt.subplots(figsize = (6,6))
#GIF
#def init():
    #ax.contourf(config[0], cmap = 'plasma')
    #ax.set_xlabel('$X$', fontdict = font)
    #ax.set_ylabel('$Y$', fontdict = font)
    #ax.set_title('Difusión, {} iteraciones, r_prom = {:3.2f}'. format(pasos, np.mean(r_list)), fontdict = font)
    #return fig,

#def animate(i):
       #im = ax.contourf(config[i], cmap = 'plasma')
       #return im,

#video = animation.FuncAnimation(fig,
               #animate,
               #init_func = init,
               #frames = pasos,
               #interval = 1)

#titulo_video = 'Difusion_mod.gif'
#video.save(titulo_video, writer = 'pillow', fps = 10)