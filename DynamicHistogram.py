import matplotlib.pyplot as plt
import numpy as np

plt.ion()

for i in range(10):
    data = np.random.randn(100)  # random data

    plt.clf()

    plt.hist(data, bins=10)
    plt.title("Dynamic Histogram")

    plt.draw()
    plt.pause(1)

plt.ioff()
plt.show()