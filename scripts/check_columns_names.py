import pandas as pd 

# Load datasets 
nasa_df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv')
eu_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv')
exo_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv')

# Print column names to confirm `planet_name` exists
print("\nNASA Columns:", nasa_df.columns.tolist())
print("\nEU Columns:", eu_df.columns.tolist())
print("\nExo Columns:", exo_df.columns.tolist())

# Check if 'planet_name' exists in all datasets
print("\nChecking if 'planet_name' exists in all datasets:")
print("'planet_name' in NASA:", 'planet_name' in nasa_df.columns)
print("'planet_name' in EU:", 'planet_name' in eu_df.columns)
print("'planet_name' in Exo:", 'planet_name' in exo_df.columns)