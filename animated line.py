import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

x_data = []
y_data = []

line, = ax.plot([], [], color='blue')

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)

plt.show()
