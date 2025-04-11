import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("Exploring Exoplanets: Analyzing Exoplanet Data with Python")

# Introduction
st.header("🌌 Introduction")
st.write("""
Exoplanets, or extrasolar planets, are planets that orbit stars outside our solar system. Since the first confirmed 
discovery in 1992, thousands of exoplanets have been identified using detection methods such as the **transit method**, 
**radial velocity**, and others. These findings have greatly expanded our knowledge of planetary systems in the universe.

This project focuses on conducting **Exploratory Data Analysis (EDA)** on exoplanet data using Python, uncovering key patterns 
and relationships in the dataset. Our aim is to visualize distributions, explore correlations between planetary and stellar 
properties, and provide an interactive interface to explore the data.
""")

# Dataset Info
st.header("🧬 Dataset")
st.write("""
We use publicly available datasets compiled from **NASA's Exoplanet Archive** and other research databases. 
These datasets contain detailed observations of confirmed exoplanets, their host stars, and discovery metadata 
(e.g., discovery method, year, and facility).
""")

# Objectives
st.header("🎯 Project Objectives")
st.markdown("""
- Understand the distribution of key exoplanet properties such as **mass**, **radius**, and **orbital period**.
- Analyze how discovery methods and trends have changed over time.
- Explore the relationship between planetary features and their host stars.
- Create an **interactive Streamlit dashboard** that allows users to visualize and explore the dataset intuitively.
""")

# Team
st.header("👩‍💻 Project Team")
st.markdown("""
- Rabia Zulfiqar  
- Jesunbo Fola-Alade  
- Yassa Azmy
""")
