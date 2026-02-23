import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]    
y = [10, 15, 7, 20, 12] 
plt.plot(x, y, marker='o', linestyle='-', color='purple')
plt.title("XY Data Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
