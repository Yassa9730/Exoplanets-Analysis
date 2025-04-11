Exoplanet Explorer: A Streamlit Data Analysis App

Video Demo: [URL HERE]
GitHub Repository: https://github.com/Yassa9730/Exoplanets-Analysis
Project Participants

1. Rabia Zulfiqar

2. Jesunbo Fola-Alade

3. Yassa Azmy

Overview
This project investigates the fascinating world of exoplanets using a combination of data science techniques and interactive visualizations. Built as a Streamlit web application, it allows users to explore, visualize, and draw insights from real exoplanet datasets in an intuitive, user-friendly interface.

Streamlit Application
Our Streamlit web app is the core user-facing feature of this project. It enables interactive exploration of the data and includes the following sections:

Pages in the App

Our Streamlit application is organized into several pages, each focusing on a specific aspect of the exoplanet data analysis process:

Home.py – Home Page
Provides an introduction to the project, background on exoplanets, and an overview of the app’s purpose and functionality.

pages/1_Exploratory_Analysis.py – Exploratory Analysis
Presents the raw dataset and offers basic descriptive statistics and exploratory plots to help users understand the underlying structure and distribution of the data.

pages/2_Visualisations.py – Key Visualizations
Showcases important trends, comparisons, and highlights discovered through the analysis. This includes charts on discovery methods, exoplanet sizes, orbital patterns, and more.

pages/3_Model_Predictions.py – Interactive Predictions
Allows users to perform custom analysis using sliders and filters. Users can explore how changing different features affects planetary classification or habitability potential (if applicable).(On Hold)

pages/4_Dashboard.py – Methodology & Sources
Summarizes the methodology used in the project, outlines key assumptions and limitations, and provides links to data sources and references.

Technologies Used in the App
Streamlit for the frontend and UI

pandas, numpy for data manipulation

matplotlib, seaborn, plotly for visualization

scikit-learn, scipy for statistical analysis and future modeling

1. Introduction
This report presents an analysis of exoplanetary datasets using data science techniques such as outlier detection, correlation analysis, and visualization. The goal is to derive meaningful insights into planetary characteristics and their relationships with stellar properties.

2. Data Cleaning and Preprocessing
2.1 Handling Limit-Flagged Values
Identified 35 columns containing limit-flagged values (e.g., <, >, min, max).

Replaced flagged values with NaN to prevent errors in numerical computations.

2.2 Outlier Detection and Handling
Applied Interquartile Range (IQR) method:

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Additional techniques used:

Modified Z-score

RobustScaler

Winsorization to retain data integrity while handling extreme values.

3. Exploratory Data Analysis (EDA)
3.1 Correlation Analysis
3.1.1 Star Mass vs. Planet Orbital Period
Spearman’s ρ: 0.086

p-value: 4.16e-76

Interpretation: Weak positive correlation. Higher star mass is slightly associated with longer planet orbital periods.

3.1.2 Planet Radius vs. Planet Mass
Spearman’s ρ: 0.058

p-value: 9.08e-36

Interpretation: Very weak positive correlation.

3.2 Box Plot Analysis
Outlier distributions were visualized using box plots, confirming the presence of extreme values in planetary mass and radius.

Winsorization was applied to adjust these values without major distortions.

4. Conclusion
This study successfully cleaned and analyzed exoplanet data, ensuring robust numerical accuracy. While certain planetary properties exhibit weak correlations, further studies could integrate additional features and machine learning models to refine predictive capabilities.

🔗 How to Run the App Locally
1. Clone the repository

2. Create a virtual environment and activate it

Install requirements:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run Home.py
