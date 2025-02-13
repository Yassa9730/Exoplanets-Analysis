import pandas as pd

# Load dataset while skipping metadata rows 
df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data.csv', skiprows=101)

# Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# Drop columns with more than 50% missing values
missing_threshold = len(df) * 0.5
df = df.dropna(thresh=missing_threshold, axis=1)

# Fill missing values in numeric columns with the median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill missing values in categorical columns with 'unknown'
for col in df.select_dtypes(include='object').columns:
    df[col].fillna('unkown', inplace=True)

# Vrify cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset 
df.to_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv', index=False)
print("\nCleaned dataset saved successfully!")