import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset nasa_exoplanets.csv
df = pd.read_csv('C:\\CS50 Final Project\\data\\nasa_exoplanets.csv', skiprows=96)

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Count discoveries by year
plt.figure(figsize=(10, 5))
df['disc_year'].value_counts().sort_index().plot(kind='bar')
plt.title('Exoplanet Discoveries by Year')
plt.xlabel('Year')
plt.ylabel('Number of Discoveries')
plt.show()


# Scatter plot for planet radius vs mass
plt.figure(figsize=(8, 5))
plt.scatter(df['pl_radj'], df['pl_bmassj'], alpha=0.5)
plt.title('Exoplanet Radius vs Mass')
plt.xlabel('Radius (Jupiter Radii)')
plt.ylabel('Mass (Jupiter Masses)')
plt.show()



