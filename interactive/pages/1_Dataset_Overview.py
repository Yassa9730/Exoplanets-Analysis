import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dataset Overview",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("/mnt/c/Users/jesun/Documents/cs50_final_project/Exoplanets-Analysis/data/exoplanets_transformed.csv")

df = load_data()

# Title
st.title("📊 Dataset Overview")

# Introductory Description
st.markdown("""
This page provides a structured overview of the exoplanet dataset used in our project. The dataset is a **merged and cleaned compilation** of exoplanet data from **three major sources**:

- `exoplanet_eu_data.csv`: [Extrasolar Planets Encyclopedia](https://exoplanet.eu/home/)
- `exoplanets.csv`: [Open Exoplanet Catalogue](https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue)
- `nasa_exoplanets.csv`: [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)

Together, these sources offer a rich and comprehensive picture of known exoplanets and their stellar systems.
""")

# Dataset Preview
st.header("🔍 Preview of the Merged Dataset")
st.dataframe(df.head(15), use_container_width=True)

# Basic Statistics
st.header("📈 Descriptive Statistics")
st.write(df.describe())

# Facility Mapping and Plot
facility_key = {
    "W. M. Keck Observatory": "Keck",
    "European Southern Observatory": "ESO",
    "Hubble Space Telescope": "HST",
    "Very Large Telescope": "VLT",
    "Spitzer Space Telescope": "Spitzer",
    "Transiting Exoplanet Survey Satellite": "TESS",
    "unknown": "Unknown Facilities"
}
df["disc_facility_short"] = df["disc_facility"].replace(facility_key)

# Sidebar Filters
st.sidebar.header("🔧 Filter Options")
year_range = st.sidebar.slider(
    "Select Discovery Year Range",
    int(df["discovery_year"].min()),
    int(df["discovery_year"].max()),
    (2000, 2025)
)
filtered_df = df[(df["discovery_year"] >= year_range[0]) & (df["discovery_year"] <= year_range[1])]


# Count discoveries per facility
st.header("🏢 Discovery Facilities Breakdown")
facility_counts = filtered_df["disc_facility_short"].value_counts()

# Plot with Rotated Labels
fig, ax = plt.subplots(figsize=(10, 5))
facility_counts.head(15).plot(kind="bar", ax=ax, color="skyblue")
ax.set_title("Top 15 Facilities by Planet Discoveries", fontsize=14)
ax.set_xlabel("Discovery Facility")
ax.set_ylabel("Number of Planets")
plt.xticks(rotation=30, ha="right", fontsize=10)

# Streamlit display
st.pyplot(fig)

# Display Abbreviation Key in Streamlit
with st.expander("🗝️ Facility Abbreviation Key"):
    st.json(facility_key)
