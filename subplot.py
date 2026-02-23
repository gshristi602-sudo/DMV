import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Height': [150, 160, 165, 170, 175, 180, 185],
    'Weight': [50, 55, 60, 65, 70, 75, 80],
    'Age': [20, 22, 24, 26, 28, 30, 32],
    'Score': [80, 85, 78, 90, 88, 92, 95]
}
df = pd.DataFrame(data)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(df['Height'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title("Height Distribution")

sns.boxplot(x=df['Weight'], ax=axes[0, 1], color='lightgreen')
axes[0, 1].set_title("Weight Boxplot")

df['Age'].value_counts().plot(kind='bar', ax=axes[1, 0], color='salmon')
axes[1, 0].set_title("Age Count")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Count")

sns.scatterplot(x='Height', y='Weight', data=df, ax=axes[1, 1], color='purple', s=100)
axes[1, 1].set_title("Height vs Weight")
axes[1, 1].set_xlabel("Height")
axes[1, 1].set_ylabel("Weight")

plt.tight_layout()
plt.show()
