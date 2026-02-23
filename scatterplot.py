import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data = {
    'Height': [150, 160, 165, 170, 175, 180, 185],
    'Weight': [50, 55, 60, 65, 70, 75, 80]
}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Height', y='Weight', data=df, color='blue', s=100)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.tight_layout()
plt.show()
