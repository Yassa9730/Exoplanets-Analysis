import pandas as pd

# Load the dataset
df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets.csv', skiprows=21)

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Drop columns with more than 50% missing values
missing_threshold = len(df) * 0.5
df = df.dropna(thresh=missing_threshold, axis=1)

# Fill missing numeric values with the median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill missing categorical values with 'unkown'
for col in df.select_dtypes(include='object').columns:
    df[col].fillna('unknown', inplace=True)


# Check that null values have been removed
print(df.isnull().sum())

print(df.head()) #View first rows
print(df.info()) #Check structure and missing values


# Save cleaned dataset 
df.to_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv', index= False)
print("\n✅ Cleaned dataset saved as 'exoplanets_cleaned.csv'")
