import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv("company_dataset1.csv", encoding="latin1")

df.columns = df.columns.str.strip().str.lower()

def extract_reviews(x):
    if pd.isna(x):
        return None
    match = re.findall(r'[\d\.]+', str(x))
    if not match:
        return None
    num = float(match[0])
    if 'k' in str(x).lower():
        return num * 1000
    return num

df['review_count_num'] = df['review_count'].apply(extract_reviews)

df['years_num'] = pd.to_numeric(
    df['years'].astype(str).str.extract(r'(\d+)')[0],
    errors='coerce'
)

def convert_employees(x):
    if pd.isna(x):
        return None

    x = str(x).lower().replace(',', '')

    if 'lakh' in x:
        return float(re.findall(r'\d+', x)[0]) * 100000
    elif 'k' in x:
        nums = re.findall(r'\d+', x)
        if len(nums) == 2:
            return (int(nums[0]) + int(nums[1])) / 2 * 1000
        elif len(nums) == 1:
            return int(nums[0]) * 1000

    return None

df['employees_num'] = df['employees'].apply(convert_employees)

df = df.dropna(subset=['employees_num', 'review_count_num', 'years_num', 'ratings'])

sns.set(style="whitegrid")

top_emp = df.sort_values(by='employees_num', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='employees_num', y='name', data=top_emp)
plt.title("Top 10 Companies by Employees")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))
plt.pie(
    top_emp['employees_num'],
    labels=top_emp['name'],
    autopct='%1.1f%%',
    startangle=140
)
plt.title("Top 10 Companies by Employees (Share)")
plt.tight_layout()
plt.show()

top_reviews = df.sort_values(by='review_count_num', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x='review_count_num', y='name', data=top_reviews)
plt.title("Top 10 Companies by Reviews")
plt.tight_layout()
plt.show()

print(df[['name', 'hq']].head(10).to_string(index=False))

top_ratings = df.sort_values(by='ratings', ascending=False).head(15)

plt.figure(figsize=(10,6))
sns.barplot(x='ratings', y='name', data=top_ratings)
plt.title("Top Companies by Ratings")
plt.tight_layout()
plt.show()

top_years = df.sort_values(by='years_num', ascending=False).head(15)

plt.figure(figsize=(10,6))
sns.barplot(x='years_num', y='name', data=top_years)
plt.title("Company Age (Years)")
plt.tight_layout()
plt.show()