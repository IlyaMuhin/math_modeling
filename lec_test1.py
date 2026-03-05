import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8
frames = 200
t = np.linspace(0, 5, frames)

# Запись диф. уравнения в виде функции
def diff_function(z, t):
    x,vx, y, vy = z
    dx_dt = vx
    dvx_dt = 10 - vx
    dy_dt = vy
    dvy_dt = -g - vy
    
    return dx_dt,dvx_dt,dy_dt,dvy_dt
# Пределы изменения переменной величины
# В данной задаче переменной величиной является время

# Определение начальных условий и параметров
alpha = 30 * np.pi / 180
v0 = 15
vx0 = v0 * np.cos(alpha)
vy0 = v0 * np.sin(alpha)
x0 = 0
y0 = 0
z0 = x0,vx0,y0,vy0



# Решение дифференциального уравнения функцией odeint
sol = odeint(diff_function, z0, t)

# Построение решения в виде графика функции
fig, ax = plt.subplots()
ball,= plt.plot([], [], 'o', color = 'r')

ball_line, = plt.plot([], [], '-', color = 'r')

def animate(i):
    ball.set_data([sol[i][0]], [sol[i][2]])
    ball_line.set_data([sol[:i, 0]], [sol[:i, 2]])

ani = FuncAnimation(fig, animate, frames = frames, interval = 30)

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('animation2.gif', writer = 'pillow')

