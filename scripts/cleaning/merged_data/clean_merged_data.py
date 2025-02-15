import pandas as pd

# Load the merged dataset 
df = pd.read_csv('C:\\CS50 Final Project\\data\\merged_exoplanets_cleaned.csv')

# Step 1: Drop coumns with more than 90% missing values
threshold = 0.90 # 90%
missing_percentage = df.isnull().mean() # Get missing percentage per column
columns_to_drop = missing_percentage[missing_percentage > threshold].index # Find columns above threshold


df.drop(columns=columns_to_drop, inplace=True) # Drop columns above threshold
print(f"✅ Dropped {len(columns_to_drop)} columns with >90% missing values.\n")

# Step 2: Fill missing values for numeric and categorical columns
numeric_cols = df.select_dtypes(include=['number']).columns 
categorical_cols = df.select_dtypes(include=['object']).columns

# Fill numeric columns with median
df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))

# Fill categorical columns with "unknown"
df[categorical_cols] = df[categorical_cols].fillna('unknown')

# Step 3: Verify that missing values are handled
print("Missing Values After Cleaning:\n", df.isnull().sum())

# Save the cleaned dataset
df.to_csv('C:\\CS50 Final Project\\data\\merged_exoplanets_final.csv', index=False)

print("✅ Saved cleaned dataset to 'merged_exoplanets_final.csv'")