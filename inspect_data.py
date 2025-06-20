import pandas as pd

# Load the dataset
df = pd.read_csv("data/processed/cleaned_students.csv")

# Show first 5 rows
print(df.head())

# Show data types
print(df.dtypes)

# Summary stats
print(df.describe())

# Unique values in Target
print("Target classes:", df['Target'].unique())


