import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.001)

def radio_function(n, t):
    dndt = - k * n * t
    return dndt


k = 0.08
n_0 = 1000

solve_Bi = odeint(radio_function, n_0, t)

plt.plot(t, solve_Bi[:, 0])


plt.savefig('test2.png')