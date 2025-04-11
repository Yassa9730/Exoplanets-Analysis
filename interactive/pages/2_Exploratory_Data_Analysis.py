import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📈",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("/mnt/c/Users/jesun/Documents/cs50_final_project/Exoplanets-Analysis/data/exoplanets_transformed.csv")

df = load_data()

# Title and Description
st.title("📈 Exploratory Data Analysis")
st.markdown("""
In this section, we explore key patterns and relationships within the exoplanet dataset.
We visualize the distribution of planetary and stellar attributes and assess correlations between important features.
""")

# Sidebar Filters
year_range = st.sidebar.slider(
    "Select Discovery Year Range",
    int(df["discovery_year"].min()),
    int(df["discovery_year"].max()),
    (2000, 2025)
)
filtered_df = df[(df["discovery_year"] >= year_range[0]) & (df["discovery_year"] <= year_range[1])]

# -- Sidebar: Discovery Method Filter --
methods = filtered_df["discovery_method"].dropna().unique()
selected_methods = st.sidebar.multiselect(
    "Select Discovery Methods",
    options=sorted(methods),
    default=sorted(methods)
)

# -- Sidebar: Planet Radius Range Filter --
radius_min = float(df["planet_radius"].min())
radius_max = float(df["planet_radius"].max())
radius_range = st.sidebar.slider(
    "Planet Radius Range (Jupiter radii)",
    min_value=radius_min,
    max_value=radius_max,
    value=(radius_min, radius_max)
)

# -- Sidebar: Orbital Period Range Filter --
period_min = float(df["planet_period"].min())
period_max = float(df["planet_period"].max())
period_range = st.sidebar.slider(
    "Orbital Period Range (days)",
    min_value=period_min,
    max_value=period_max,
    value=(period_min, period_max)
)

# -- Sidebar: Log Scale Toggle --
use_log = st.sidebar.checkbox("Use Log Scale for Axes", value=True)

# -- Apply All Filters --
method_filtered_df = filtered_df[
    (filtered_df["discovery_method"].isin(selected_methods)) &
    (filtered_df["planet_radius"] >= radius_range[0]) &
    (filtered_df["planet_radius"] <= radius_range[1]) &
    (filtered_df["planet_period"] >= period_range[0]) &
    (filtered_df["planet_period"] <= period_range[1])
]

# -- Plot --
st.subheader("🪐 Planet Radius vs. Orbital Period by Discovery Method")
st.markdown("This interactive scatter plot helps explore how detection methods vary by planet size and orbital distance.")

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=method_filtered_df,
    x="planet_period",
    y="planet_radius",
    hue="discovery_method",
    palette="tab10",
    alpha=0.7,
    ax=ax
)

# Apply axis scaling
ax.set_xlabel("Orbital Period (days)")
ax.set_ylabel("Planet Radius (Jupiter radii)")
ax.set_title("Planet Radius vs. Orbital Period by Discovery Method")

if use_log:
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Orbital Period (days) [log scale]")
    ax.set_ylabel("Planet Radius (Jupiter radii) [log scale]")

ax.legend(title="Discovery Method", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)


# Handle outliers for visualizations
filtered_df = filtered_df[filtered_df["planet_period"] < 10000]  # Filter extreme orbital periods
filtered_df = filtered_df[filtered_df["mass"] < filtered_df["mass"].quantile(0.99)]  # Remove extreme planet masses

# Distribution Plot: Planet Radius
st.subheader("🪐 Distribution of Planet Radius")
fig1, ax1 = plt.subplots()
sns.histplot(filtered_df["planet_radius"], bins=50, kde=True, ax=ax1, color="purple")
ax1.set_xlabel("Planet Radius (Jupiter radii)")
ax1.set_ylabel("Frequency")
ax1.set_title("Distribution of Planet Radius")
st.pyplot(fig1)

# Scatter Plot: Star Mass vs. Orbital Period
st.subheader("🌟 Star Mass vs. Orbital Period")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x="star_mass", y="planet_period", alpha=0.6, ax=ax2)
ax2.set_xlabel("Star Mass (Solar masses)")
ax2.set_ylabel("Planet Orbital Period (days)")
ax2.set_title("Correlation Between Star Mass and Planet Orbital Period")
st.pyplot(fig2)

# Boxplot: Planet Mass (Log Scale)
st.subheader("📦 Outlier Detection - Planet Mass (Log Scaled)")
fig3, ax3 = plt.subplots()
sns.boxplot(x=np.log1p(filtered_df["mass"]), ax=ax3, color="skyblue")
ax3.set_xlabel("Log(1 + Planet Mass) [Jupiter mass]")
ax3.set_title("Box Plot of Planet Mass (Log Scaled)")
st.pyplot(fig3)

# Correlation Heatmap
st.subheader("🔗 Correlation Heatmap of Key Numerical Features")

# Select only relevant numerical columns
selected_cols = [
    "planet_radius", "planet_period", "semi_major_axis", "mass",
    "star_mass", "star_radius", "st_tefferr1", "st_met"
]

# Drop missing if any
filtered_numeric = filtered_df[selected_cols].dropna()

fig4, ax4 = plt.subplots(figsize=(12, 10))
sns.heatmap(filtered_numeric.corr(method='spearman'), cmap='coolwarm', annot=True, fmt=".2f", ax=ax4)
ax4.set_title("Spearman Correlation Heatmap")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
st.pyplot(fig4)

# Summary
st.markdown("""
These visualizations help uncover patterns in the data, such as the presence of outliers,
or how certain planetary characteristics (like orbital period) may be loosely correlated with their host stars.
""")
