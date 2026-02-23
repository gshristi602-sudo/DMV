import matplotlib.pyplot as plt
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 40, 15, 20]
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue')
plt.title("Fruit Count")
plt.xlabel("Fruit")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()
