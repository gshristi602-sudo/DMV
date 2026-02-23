import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [120, 150, 170, 130, 180]

plt.plot(days, sales, marker='o', linestyle='-', color='blue')

plt.title("Weekly Sales Overview")
plt.xlabel("Days of the Week")
plt.ylabel("Sales Amount")

plt.grid(True)

plt.show()
