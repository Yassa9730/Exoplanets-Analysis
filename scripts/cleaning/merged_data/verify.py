import pandas as pd

# Load the final cleaned dataset 
df = pd.read_csv('C:\\CS50 Final Project\\data\\merged_exoplanets_final.csv')

# Check dataset structure
print("\n🔍 Dataset Information: ")
print(df.info())

# Summary statistics
print("\n📊 Summary Statistics: ")
print(df.describe())