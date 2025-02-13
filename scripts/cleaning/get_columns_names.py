import pandas as pd

# Load daatsets
nasa_df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv')
eu_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv')
exo_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv')

# Print column names to compare 
print("\nNASA Columns:", nasa_df.columns)
print("\nEU Columns:", eu_df.columns)
print("\nExo Columns:", exo_df.columns)

