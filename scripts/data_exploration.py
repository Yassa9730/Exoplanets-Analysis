import pandas as pd

#Load the dataset nasa_exoplanets.csv
df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets.csv', skiprows=96)

#Display the first few rows
print("First 5 Rows of the Dataset:")
print(df.head())

#check the structure of the dataset
print("\nDataset Information:")
print(df.info())

#check for missing values 
print("\nMissiing Values in Each Column:")
print(df.isnull().sum())