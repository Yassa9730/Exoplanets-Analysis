import pandas as pd

# Load the dataset
df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets.csv', skiprows=21 )

# Calculate the precentage of missing values for each column 
missing_percent = df.isnull().mean() / len(df) * 100

# Display columns where more than 50% of the values are missing
high_missing = missing_percent[missing_percent > 50]

print("Columns with more than 50% missing values:")
print(high_missing)


# Check missing values for numeric coolumns
numeric_missing = df.select_dtypes(include=['number']).isnull().sum()
numeric_missing = numeric_missing[numeric_missing > 0]  #Only show columns with missing values
print("\nMissing Values in Numeric Columns:")
print(numeric_missing)


# Check missing values for categorical columns
categorical_missing = df.select_dtypes(include=['object']).isnull().sum()
categorical_missing = categorical_missing[categorical_missing > 0]  #Only show columns with missing values
print("\nMissing Values in Categorical Columns:")
print(categorical_missing)