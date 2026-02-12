import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**6, 100)

def radio_function(n, t):
    dndt = 1/(k * n)
    return dndt


k = 0.000001
n_0 = 1

solve_Bi = odeint(radio_function, n_0, t)

plt.plot(t, solve_Bi[:, 0])


plt.savefig('test1.png')