# Step 1: Setup and Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Improve plot aesthetics
sns.set(style="whitegrid")

# Step 2: Load the Dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and structure
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 3: Clean the Dataset (if needed)
df.fillna(df.mean(), inplace=True)  # Fill missing values
# Or use df.dropna(inplace=True) to drop missing rows

# Step 4: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

# Group by species and compute mean of numerical columns
species_group = df.groupby('species').mean()
print("\nMean values per species:")
print(species_group)

# Step 5: Data Visualization

# 5.1 Line Chart (Cumulative Sepal Length)
plt.figure(figsize=(8,5))
plt.plot(df['sepal length (cm)'].cumsum(), label='Cumulative Sepal Length', color='blue')
plt.title('Cumulative Sepal Length')
plt.xlabel('Index')
plt.ylabel('Cumulative Length (cm)')
plt.legend()
plt.show()

# 5.2 Bar Chart (Average Petal Length per Species)
plt.figure(figsize=(8,5))
species_group['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.show()

# 5.3 Histogram (Distribution of Sepal Width)
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# 5.4 Scatter Plot (Sepal Length vs Petal Length)
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', s=100)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# Step 6: Findings / Observations
print("\nObservations:")
print("- Setosa has significantly shorter petals and smaller sepal length.")
print("- Versicolor and Virginica have overlapping sepal lengths, but different petal lengths.")
print("- Scatter plot shows clear separation between species based on petal length.")

# Step 7: Save Dataset (Optional)
df.to_csv('iris_analysis.csv', index=False)
df.fillna(df.mean(), inplace=True)  # Fill missing values
# Fill missing values only for numeric columns
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
