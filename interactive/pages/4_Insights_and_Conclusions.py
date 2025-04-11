import streamlit as st

st.set_page_config(
    page_title="Insights and Conclusions",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Insights and Conclusions")

st.markdown("""
This section summarizes key insights and takeaways derived from the exploratory data analysis of our exoplanet dataset.
We reflect on observed patterns, relationships between variables, and interesting anomalies.
""")

st.subheader("📌 Key Observations")

st.markdown("""
- **Planet Radius and Orbital Period**:
  - Most planets discovered are small with short orbital periods.
  - Detection bias likely favors planets that are large and close to their stars, especially for transit and radial velocity methods.

- **Discovery Method Patterns**:
  - Transit and radial velocity are the dominant discovery techniques.
  - Transit methods detect more small-radius, short-period planets, while radial velocity finds a broader range.

- **Planet Mass Distribution**:
  - Masses are heavily skewed. A few planets are extremely massive.
  - After applying a log scale, we observe a more normalized distribution with clear outliers.

- **Star Mass vs. Planet Period**:
  - Some correlation is suggested — larger stars may have more distant or faster-orbiting planets, but it's not a strong linear trend.

- **Correlations**:
  - **Planet Radius and Mass** show moderate positive correlation.
  - **Orbital Period** correlates weakly with other features, showing its independence.
  - Star properties like mass, radius, and metallicity relate to each other but weakly link to planetary characteristics.
""")

st.subheader("📦 Interpreting the Box Plot of Planet Mass")

st.markdown("""
The box plot in the EDA section visualized the **distribution of planet masses (in Jupiter masses)** using a **log scale**:

- The central box captures the middle 50% of planets — the interquartile range.
- The median planet mass is marked by a line within the box.
- Points outside the whiskers represent **outliers** — extremely massive planets, some of which may be brown dwarfs or stellar companions.
- Using `log1p` transformation (log of 1 + mass) helped manage skew and made the distribution easier to interpret.
""")

st.subheader("🔚 Conclusion")

st.markdown("""
The EDA phase has provided a clearer understanding of the dataset’s structure, common planetary properties, and how discoveries are shaped by detection methods.
This forms a strong foundation for deeper statistical modeling or predictive analysis.
""")
