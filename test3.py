import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

def radio_function(v, t):
    dvdt = a_0 - (v**2 * k) /m
    return dvdt
    
    

m = 0.5
k = 0.1
v_0 = 0
a_0 = 1.5

solve_Bi = odeint(radio_function, v_0, t)

plt.plot(t, solve_Bi[:, 0])


plt.savefig('test3.png')