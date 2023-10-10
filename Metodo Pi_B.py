import numpy as np
import matplotlib.pyplot as plt

#Numero de iteraciones
steps = [1E3, 5E3, 1E4, 5E4, 1E5, 1.5E5]
rand = np.random

#Desplazamiento
dx, dy = 0.15, 0.15

def metodo_B(step):
       x, y = rand.uniform(-1,1, size=(2,1))
       #Recalculando puntos
       for i in range(1,int(step)):
              expr = False
              while expr is False:
                     xn = x[-1] + rand.uniform(-1,1)*dx
                     yn = y[-1] + rand.uniform(-1,1)*dy
                     expr = abs(xn)<=1 and abs(yn)<=1 # Condicional Punto Dentro
                     if expr == True:
                            x = np.append(x, xn)
                            y = np.append(y, yn)       

       Circulo = x**2 + y**2 <= 1
       Cuadrado = np.invert(Circulo)
       pi = 4*Circulo.sum()/i
       err = err = 100*abs(pi - np.pi)/np.pi

       return pi, err, Circulo, Cuadrado, x, y

pi_plot = []
B = []
for step in steps:
       pi, err, Circulo, Cuadrado, x, y = metodo_B(step)
       B.append(pi)
       print(pi)
       pi_plot.append(np.pi)
       
       plt.title('Metodo B: ' + str(int(step)) + " iteraciones")
       plt.plot(x[Circulo], y[Circulo], 'b.')
       plt.plot(x[Cuadrado], y[Cuadrado], 'r.')
       plt.plot(0, 0, label='$\pi$ = {:4.4f}\nerror = {:4.4f}%'.format(pi,err), alpha=0)
       plt.axis('square')
       plt.legend(frameon=True, framealpha=0.9, fontsize=12)
       plt.show()
       

plt.title("Simulaciones")
plt.plot(steps, A, '-b.')
plt.plot(steps, pi_plot, 'r')
plt.show()

