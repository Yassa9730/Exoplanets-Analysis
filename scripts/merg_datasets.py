import pandas as pd

#Load datasets
nasa_df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets.csv', skiprows=96)
eu_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanet_eu_data.csv')
exoplanet_df = pd.read_csv('C:\\CS50 Final Project\\data\\exoplanets.csv')


#Display column names
print("NASA Dataset Columns:", nasa_df.columns)
print("EU Dataset Columns:", eu_df.columns)
print("Exoplanet Dataset Columns:", exoplanet_df.columns)