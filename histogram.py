import matplotlib.pyplot as plt
marks = [55, 70, 75, 60, 90, 85, 72, 88, 95, 67, 73, 80, 78, 69, 92]
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
