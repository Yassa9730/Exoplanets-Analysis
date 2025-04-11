# 🌌 Exoplanet Explorer: A Streamlit Data Analysis App

**Video Demo:** [URL HERE]  
**GitHub Repository:** https://github.com/Yassa9730/Exoplanets-Analysis

---

## 👥 Project Participants

1. Rabia Zulfiqar  
2. Jesunbo Fola-Alade  
3. Yassa Azmy

---

## 🧠 Overview

This project investigates the fascinating world of exoplanets using a combination of data science techniques and interactive visualizations. Built as a Streamlit web application, it allows users to explore, visualize, and draw insights from real exoplanet datasets in an intuitive, user-friendly interface.

---

## 💻 Streamlit Application

Our Streamlit web app is the core user-facing feature of this project. It enables interactive exploration of the data and includes the following sections:

---

## 📄 Pages in the App

### `Home.py` – **Home Page**
Provides an introduction to the project, background on exoplanets, and an overview of the app’s purpose and functionality.

---

### `pages/1_Dataset_Overview.py` – **Dataset Overview**
Presents the cleaned and transformed dataset and offers basic statistics and dataset previews. Also includes visualizations showing how many exoplanets were discovered by each facility.

---

### `pages/2_Exploratory_Data_Analysis.py` – **Exploratory Data Analysis**
Showcases key trends and comparisons through visualizations. Includes filters, scatter plots, histograms, box plots, and correlation heatmaps to explore relationships between features such as planet radius, orbital period, and star mass.

---

### `pages/3_Model_Predictions.py` – **Model Predictions (Coming Soon)**
Reserved for machine learning functionality. Will allow users to explore predicted values or classifications based on planetary features. Currently not implemented.

---

### `pages/4_Insights_and_Conclusions.py` – **Insights and Conclusions**
Summarizes the findings from EDA, interprets results from visualizations, and reflects on the implications of the analysis.

---

## ⚙️ Technologies Used in the App

- **Streamlit** for the frontend and UI  
- **pandas, numpy** for data manipulation  
- **matplotlib, seaborn, plotly** for visualization  
- **scikit-learn, scipy** for statistical analysis and future modeling  

---

## 📊 1. Introduction

This report presents an analysis of exoplanetary datasets using data science techniques such as outlier detection, correlation analysis, and visualization. The goal is to derive meaningful insights into planetary characteristics and their relationships with stellar properties.

---

## 🧹 2. Data Cleaning and Preprocessing

### 2.1 Handling Limit-Flagged Values

- Identified 35 columns containing limit-flagged values (e.g., `<`, `>`, min, max).  
- Replaced flagged values with `NaN` to prevent errors in numerical computations.

### 2.2 Outlier Detection and Handling

Applied the **Interquartile Range (IQR)** method:

```
Lower Bound = Q1 - 1.5 × IQR  
Upper Bound = Q3 + 1.5 × IQR
```

**Additional techniques:**

- Modified Z-score  
- RobustScaler  
- Winsorization to retain data integrity while handling extreme values

---

## 🔍 3. Exploratory Data Analysis (EDA)

### 3.1 Correlation Analysis

#### 3.1.1 Star Mass vs. Planet Orbital Period

- Spearman’s ρ: 0.086  
- p-value: 4.16e-76  
- **Interpretation:** Weak positive correlation

#### 3.1.2 Planet Radius vs. Planet Mass

- Spearman’s ρ: 0.058  
- p-value: 9.08e-36  
- **Interpretation:** Very weak positive correlation

### 3.2 Box Plot Analysis

- Outlier distributions were visualized using box plots  
- Confirmed extreme values in planetary mass and radius  
- Winsorization applied to reduce outlier impact

---

## ✅ 4. Conclusion

This study successfully cleaned and analyzed exoplanet data, ensuring robust numerical accuracy. While certain planetary properties exhibit weak correlations, further studies could integrate additional features and machine learning models to refine predictive capabilities.

---

## 🛠️ How to Run the App Locally

1. Clone the repository  
2. Create and activate a virtual environment  
3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run Home.py
```

---
