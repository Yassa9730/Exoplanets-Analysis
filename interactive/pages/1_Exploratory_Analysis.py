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
    return pd.read_csv("/mnt/c/Users/jesun/Documents/cs50_final_project/Exoplanets-Analysis/data/merged_exoplanets_final.csv")

df = load_data()

st.write("# 🔍 Exploratory Data Analysis")
st.text("Interactively explore the exoplanet dataset using filters and statistics")

st.write("## Dataset Preview")
st.dataframe(df.head(15))

st.write("### Basic Statistics")
st.write(df.describe())

st.write("### Dataset Info")
st.write(df.info())

