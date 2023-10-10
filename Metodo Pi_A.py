import numpy as np
import matplotlib.pyplot as plt

steps = [1E3, 5E3, 1E4, 5E4, 1E5, 1.5E5]

def metodo_A(step):
       x,y = np.random.uniform(-1, 1, size=(2, int(step)))
       Circulo = (x**2 + y**2) <= 1   # Lista TRUE o FALSE si cumple la desigualdad
       Cuadrado = np.invert(Circulo)  # Invierte la lista del Circulo en TRUE o FALSE
       
       pi = 4*Circulo.sum()/step
       err = 100*abs(pi - np.pi)/np.pi
       return pi, err, Circulo, Cuadrado, x, y

pi_plot = []
A = []
for step in steps:
       pi, err, Circulo, Cuadrado, x, y = metodo_A(step)
       A.append(pi)
       print(f'pi = {pi}, \t  error = {err}')
       pi_plot.append(np.pi)
       
       plt.title( 'Metodo A: ' + str(int(step)) + " iteraciones")
       plt.plot(x[Circulo], y[Circulo], 'b.')
       plt.plot(x[Cuadrado], y[Cuadrado], 'r.')
       plt.plot(0, 0, label='$\pi$ = {:4.4f}\nerror = {:4.4f}%'
                .format(pi,err), alpha=0)
       plt.axis('square')
       plt.legend(frameon=True, framealpha=0.9, fontsize=12)
       plt.show()
       
plt.plot(steps, A, '-ro')
plt.plot(steps, pi_plot)
plt.title('Metodo B')
plt.xlabel('Iteraciones')
plt.ylabel('Aproximacio a $\\pi$')
plt.show()





              

