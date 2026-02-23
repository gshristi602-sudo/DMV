import matplotlib.pyplot as plt

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 40, 15, 20]

plt.ion()
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(categories, values, color='skyblue')
ax.set_title("Fruit Count")
ax.set_xlabel("Fruit")
ax.set_ylabel("Quantity")
plt.tight_layout()
plt.show()

for i in range(5):
    values = [v + i*2 for v in values]
    for bar, val in zip(bars, values):
        bar.set_height(val)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.5)

plt.ioff()
plt.show()
