import pandas as pd

# Load the dataset and skip metadata rows 

df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets.csv', skiprows=96)

# Display first few rows to verify
print("First 5 rows after removing metadata:")
print(df.head())

# Save the cleaned dataset 
df.to_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv', index=False)

print("✅ Cleaned dataset saved as 'nasa_exoplanets_cleaned.csv' successfully!")