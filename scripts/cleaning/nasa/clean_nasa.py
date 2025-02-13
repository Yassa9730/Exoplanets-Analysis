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

#Handle missing values

#Drop columns with more than 50% missing values
missing_threshold = len(df) * 0.5
df = df.dropna(thresh=missing_threshold, axis=1)

#Fill numeric comumns with the median
df.fillna(df.median(numeric_only=True), inplace=True)

#Fill categorical columns with the 'unkown'
for col in df.select_dtypes(include='object').columns:
    df[col].fillna('unknown', inplace=True)

#check the remaining missing values
print("\nMissing Values After cleaning")
print(df.isnull().sum())