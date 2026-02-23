import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

x, y = 5, 5
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

def on_key(event):
    global x, y

    if event.key == 'up':
        y += 0.5
    elif event.key == 'down':
        y -= 0.5
    elif event.key == 'left':
        x -= 0.5
    elif event.key == 'right':
        x += 0.5

    circle.center = (x, y)
    fig.canvas.draw()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.title("Use Arrow Keys to Move the Circle")
plt.show()
