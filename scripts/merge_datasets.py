import pandas as pd

# Load datasets
nasa_df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv')
eu_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv')
exo_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv')

# Merge NASA and EU datasets first
merged_df = pd.merge(nasa_df, eu_df, on=['planet_name', 'star_name', 'discovery_year'], how='outer')

# Merge with the Exoplanet dataset
merged_f = pd.merge(merged_df, exo_df, on=['planet_name', 'star_name', 'discovery_year'], how='outer')

# Save the final merged dataset
merged_f.to_csv('C:\\CS50 Final Project\\data\\merged_exoplanets.csv', index=False)

print("✅ Merged datasets saved as 'merged_exoplaneets.csv'")


