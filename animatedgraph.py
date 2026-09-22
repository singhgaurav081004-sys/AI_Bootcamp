import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 200)
line, = ax.plot(x, np.sin(x), color='crimson', lw=2)

line.set_ydata(np.cos(x))

from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 200)
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x), lw=3)
ax.set_ylim(-1.2, 1.2)

def update(phase):
    line.set_ydata(np.sin(x + phase))
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, np.pi/2, 60),
                    interval=40, blit=True)

plt.show()
