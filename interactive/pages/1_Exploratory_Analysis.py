import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="🔍",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("/mnt/c/Users/jesun/Documents/cs50_final_project/Exoplanets-Analysis/data/exoplanets_transformed.csv")

df = load_data()

st.write("# 🔍 Exploratory Data Analysis")
st.text("Interactively explore the exoplanet dataset using filters and statistics")

st.write("## Dataset Preview")
st.dataframe(df.head(15))

st.write("### Basic Statistics")
st.write(df.describe())

st.write("### Dataset Info")

# Facility Name Mapping
facility_key = {
    "W. M. Keck Observatory": "Keck",
    "European Southern Observatory": "ESO",
    "Hubble Space Telescope": "HST",
    "Very Large Telescope": "VLT",
    "Spitzer Space Telescope": "Spitzer",
    "Transiting Exoplanet Survey Satellite": "TESS",
    "unknown": "Unknown Facilities"
}

# Replace facility names with abbreviations
df["disc_facility_short"] = df["disc_facility"].replace(facility_key)

# Sidebar Filters
st.sidebar.header("Filter Options")
year_range = st.sidebar.slider(
    "Select Discovery Year Range",
    int(df["discovery_year"].min()),
    int(df["discovery_year"].max()),
    (2000, 2025)
)
filtered_df = df[(df["discovery_year"] >= year_range[0]) & (df["discovery_year"] <= year_range[1])]

# Count discoveries per facility
facility_counts = filtered_df["disc_facility_short"].value_counts()

# Plot with Rotated Labels
fig, ax = plt.subplots(figsize=(10, 5))
facility_counts.head(15).plot(kind="bar", ax=ax, color="skyblue")
ax.set_title("Top 15 Facilities by Planet Discoveries")
ax.set_xlabel("Discovery Facility")
ax.set_ylabel("Number of Planets")
plt.xticks(rotation=30, ha="right", fontsize=10)  # Rotate for better readability

# Streamlit display
st.pyplot(fig)

# Display Abbreviation Key in Streamlit
st.text("Facility Name Key")
st.json(facility_key)

