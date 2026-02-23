import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [2000, 2500, 2200, 2700, 3000, 2800]

plt.plot(months, revenue, marker='o', color='green')

plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.grid(True)

plt.show()
