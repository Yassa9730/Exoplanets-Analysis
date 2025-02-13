import pandas as pd
import re

# Load merged dataset
df = pd.read_csv('C:\\CS50 Final Project\\data\\merged_exoplanets.csv')

# Function to extract author & year
def clean_reference(ref):
    if pd.isna(ref): #If the value is Nan, return as is
        return ref
    match = re.search(r'>(.*?)</a>', ref) #Extract text inside <a> tags
    return match.group(1) if match else ref # Return extracted text or original value

# Apply cleaning function to reference columns
for col in ['pl_refname', 'st_refname', 'sy_refname']:
    df[col] = df[col].apply(clean_reference)

# Save cleaned dataset 
df.to_csv('C:\\CS50 Final Project\\data\\merged_exoplanets_cleaned.csv', index=False)

print("✅ Cleaned dataset saved as 'merged_exoplanets_cleaned.csv'")