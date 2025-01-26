import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("iris.csv")

# Clean column names by stripping unnecessary spaces and quotes
df.columns = df.columns.str.strip().str.replace('"', '')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check and display cleaned column names
print("\nCleaned Column names in the dataset:")
print(df.columns)

# Visualize the distribution of Height (Inches)
plt.figure(figsize=(8, 5))
sns.histplot(df["Height(Inches)"], kde=True, color="blue")
plt.title("Distribution of Height (Inches)")
plt.xlabel("Height (Inches)")
plt.ylabel("Frequency")
plt.show()

# Visualize the distribution of Weight (Pounds)
plt.figure(figsize=(8, 5))
sns.histplot(df["Weight(Pounds)"], kde=True, color="green")
plt.title("Distribution of Weight (Pounds)")
plt.xlabel("Weight (Pounds)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot between Height and Weight
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Height(Inches)", y="Weight(Pounds)", data=df, color="red")
plt.title("Height vs Weight")
plt.xlabel("Height (Inches)")
plt.ylabel("Weight (Pounds)")
plt.show()
