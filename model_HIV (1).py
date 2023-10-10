#!/usr/bin/env python
# coding: utf-8

# In[72]:


# Computational Nanotechnology Applications
# Proyect 1 - 12/08/2021 
#Jair Dominguez, Jesús Flores, Adriel Reyes
# One model of viral load HIV 

#Import mathematical libraries and graphics
import numpy as np
import matplotlib.pyplot as plt

experimental_data = np.loadtxt("HIVseries.csv", delimiter=',') #Import experimental data

# Create the arrays for the temporal dates and viral load
time_days = np.zeros(len(experimental_data))
time_days = experimental_data[:,0]
print("Time in days =",time_days)
viral_load = np.zeros(len(experimental_data))
viral_load = experimental_data[:,1]
print("Viral load of HIV = ",viral_load)


t = np.linspace(0,10,101)# Temporal values for the function V(t) 

# Constants, random values,depend of model. Manual adjuste
A = 87500 
α = 0.2625
B = 87500
β = 0.9564
inverse=1/α # New constant to v2

V = A*np.exp(-α*t)+B*np.exp(-β*t) # V=viral load after medication
V2 = A*np.exp(-inverse*t)+B*np.exp(-β*t) # invese of the T-cell infection rate

plt.plot(t,V,"g",label="$V(t)=Ae^{-α t}+Be^{-β t}$") # graphic of the function V(t)
plt.plot(time_days, viral_load, "r+",label="Experimental data") # graphic experimental dates
plt.plot(t,V2,"b", label="Inverse of the T-cell infection rate") # graphic of inverse of T-cell infection rate
# Details of the graphic
plt.title("Model of viral load for HIV after medication",size=12,weight="bold")
plt.xlabel("Time (days)")
plt.ylabel("Viral load (N/ml) ")
plt.text(3,75000, "A=87500, α= 0.2625, B=875000, β=0.9564", fontsize=8, color='green')
plt.text(4,50000, "A=87500, α=1/α, B=875000, β=0.5  ", fontsize=8, color='blue')
plt.legend()
plt.grid()
plt.savefig("grafica_V.jpg") # Keep the graphic


# In[19]:


# Model of genetic switching in bacteria
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,30)  # Create a variable of time

def W(time,A,τ): # Definimos la función W(t)
    return A*(np.exp((-time/τ)) + time/τ - 1) # A and τ are constants

W1 = W(t,1,1) # take A=1 y τ=1

plt.plot(t,W1,"blue",label="$W(t)=(e^{-t}+t-1$")
plt.xlabel("t")
plt.ylabel("W(t)")
plt.text(0,0.9, "A=1, τ=1", fontsize=10, color='blue')
plt.legend()
plt.savefig("grafica_W_funcion.jpg")
              


# In[68]:


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,30)  # Create a variable of time

def W(time,A,τ): # Definimos la función W(t)
    return A*(np.exp((-time/τ)) + time/τ - 1) # A and τ are constants

W1 = np.zeros(len(t))
W2 = np.zeros(len(t))
W3 = np.zeros(len(t))
W4 = np.zeros(len(t))
W5 = np.zeros(len(t))
W6 = np.zeros(len(t))
W7 = np.zeros(len(t))
W8 = np.zeros(len(t))
W9 = np.zeros(len(t))

W1 = W(t,1,1)
W2 = W(t,10,-0.5) 
W3 = W(t,-10,-0.5)
W4 = W(t,-20,0.5)
W5 = W(t,20,0.5)
W6 = W(t,-5,30)
W7 = W(t,5,-30)
W8 = W(t,100,1)
W9 = W(t,-100,-1)

plt.plot(t,W1,"k",label="A=1, τ=1")
plt.plot(t,W2,"--",label="A=10 τ=-0.5")
plt.plot(t,W3,"-.",label="A=-10 τ=-0.5")
plt.plot(t,W4,":",label="A=-20 τ=0.5")
plt.plot(t,W5,".",label="A=20 τ=0.5")
plt.plot(t,W6,"x",label="A=-5 τ=30")
plt.plot(t,W7,"+",label="A=5 τ=-30")
plt.plot(t,W8,"h",label="A=100 τ=1")
plt.plot(t,W9,label="A=-100 τ=-1")

plt.title("$W(t)=A(e^{-t/τ}+ t/τ -1)$")
plt.xlabel("t")
plt.ylabel("W(t)")
plt.xlim(0,3)
plt.legend()
plt.grid()
plt.savefig("grafica_varias_W.jpg")


# In[45]:


# Graphic experimental data and W(t) function
import numpy as np
import matplotlib.pyplot as plt

experimental_data = np.loadtxt("g149novickB.csv", delimiter=',') # Export the data

time_hours = np.zeros(12)
time_hours = experimental_data[0:12,0]
print("Time in hours. The e-folding time was about 3 hours =",time_hours)
fraction_β = np.zeros(12)
fraction_β = experimental_data[0:12,1]
print("Fraction of maximum beta-galactosidase activity =",fraction_β)
time = np.linspace(np.amin(time_hours),np.amax(time_hours),len(fraction_β))
def W(t,τ,A):
    return A*(np.exp((-t/τ)) + t/τ - 1 )

plt.plot(time_hours,fraction_β,"mv",label="Experimental data")
plt.plot(time,W(time,34,3.5),label="Theoretical model $W(t)$")
plt.title("$W(t)=A(e^{-t/τ} + t/τ - 1 )$")
plt.xlabel("Time (hours)")
plt.ylabel("Fraction of max β-galactosidase act.")
plt.legend()
plt.grid()
plt.text(3,0.10, "A=34 τ=3.5", fontsize=12, color='magenta')
plt.savefig("grafica_experimento_W.jpg")


# In[73]:


# Graphic experimental data and V(t) function

experimental_data = np.loadtxt("g149novickA.csv", delimiter=',') # Export the data
# Create the arrays for the temporal dates and viral load
time_hours = np.zeros(len(experimental_data))
time_hours = experimental_data[:,0]
print("Time in hours =",time_hours)
fraction_galactoside= np.zeros(len(experimental_data))
fraction_galactoside = experimental_data[:,1]
print("Fraction of maximum beta-galactosidase activity = ",fraction_galactoside)

time2 = np.linspace(np.amin(experimental_data),np.amax(time_hours),len(experimental_data)) # Temporal variable

def V(t,τ):
    return 1 - np.exp(-t/τ)



plt.plot(time_hours,fraction_galactoside,"m+",label="Experimental data")
plt.plot(time2,V(time2,3.50),"y",label="V(t)=1-e^{-t/τ}") # Using τ=3.50
plt.title("Model of genetic switching in bacteria")
plt.xlabel("Time (Hours)")
plt.ylabel("Fraction of max β-galactosidase")



plt.legend()
plt.grid()
plt.text(0,0.7, "τ=3.50", fontsize=12, color='yellow')
plt.savefig("grafica_experimento_V.jpg")


# In[119]:


import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,30)  # Create a variable of time

def V(time,τ): # Definimos la función W(t)
    return 1 - np.exp((-time/τ))  # τ is constant

V1 = np.zeros(len(t))
V2 = np.zeros(len(t))
V3 = np.zeros(len(t))
V4 = np.zeros(len(t))
V5 = np.zeros(len(t))
V6 = np.zeros(len(t))
V7 = np.zeros(len(t))
V8 = np.zeros(len(t))
V9 = np.zeros(len(t))

V1 = V(t,0.1)
V2 = V(t,0.3) 
V3 = V(t,0.5)
V4 = V(t,1)
V5 = V(t,1.5)
V6 = V(t,3.5)
V7 = V(t,5)
V8 = V(t,10)
V9 = V(t,50)

plt.plot(t,V1,"k",label="τ=0.1")
plt.plot(t,V2,"--",label="τ=0.3")
plt.plot(t,V3,"-.",label="τ=0.5")
plt.plot(t,V4,":",label="τ=1")
plt.plot(t,V5,".",label="τ=1.5")
plt.plot(t,V6,"x",label="τ=3.5")
plt.plot(t,V7,"+",label="τ=5")
plt.plot(t,V8,"h",label="τ=10")
plt.plot(t,V9,label="τ=50")

plt.title("$V(t)=1-e^{-t/τ}$")
plt.xlabel("t")
plt.ylabel("V(t)")
plt.legend()
plt.grid()
plt.savefig("grafica_varias_V.jpg")


# In[ ]:




