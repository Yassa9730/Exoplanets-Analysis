import pandas as pd

# Load the data
df = pd.read_csv('C:\\CS50 Final Project\\data\\merged_exoplanets_cleaned.csv')

# Display the first few rows
print("First 5 Rows of the Dataset:")
print(df.head())

# Check the structure of the dataset
print("\nDataset Information:")
print(df.info())

# Check for missing values 
print("\nMissiing Values in Each Column:")
print(df.isnull().sum())

# Calculate missinv value percentage
missing_percentage = (df.isnull().sum() / len(df)) * 100

# Show only columns with missing values
missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)

# Display results
print("\nPercentage of Missing Values in Each Column:")
print(missing_percentage)