import pandas as pd

# Load datasets
nasa_df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv')
eu_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv')
exo_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv')

# Standardize column names
nasa_df.rename(columns={
    'pl_name': 'planet_name',
    'hostname': 'star_name',
    'disc_year': 'discovery_year',
    'st_mass': 'star_mass',
    'st_rad': 'star_radius',
    'st_teff': 'star_temperature',
    'st_metfe': 'star_metallicity',
    'pl_rade': 'planet_radius',
    'pl_orbper': 'planet_period',
    'pl_orbsmax': 'semi_major_axis',
    'discoverymethod': 'discovery_method',
}, inplace=True)


eu_df.rename(columns={
    'name': 'planet_name',
    'discovered': 'discovery_year',
    'radius': 'planet_radius',
    'orbital_period': 'planet_period',
    'semi_major_axis': 'semi_major_axis',
    'detection_type': 'discovery_method'
}, inplace=True)

exo_df.rename(columns={
    'planet_name': 'planet_name',
    'discovery_year': 'discovery_year',
    'planet_radius': 'planet_radius',
    'planet_period': 'planet_period',
    'planet_semimajoraxis': 'semi_major_axis',
    'discovery_method': 'discovery_method'
}, inplace=True)


# Verify the new column names
print("\nNASA Columns:", nasa_df.columns)
print("\nEU Columns:", eu_df.columns)
print("\nExo Columns:", exo_df.columns)


# Save the renamed datasets
nasa_df.to_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets_cleaned.csv', index=False)
eu_df.to_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data_cleaned.csv', index=False)
exo_df.to_csv('C:\\CS50 Final Project\\data\\exoplanets_cleaned.csv', index=False)

print("✅ Column names standardized and datasets saved")