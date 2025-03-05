### **Correlation Analysis Report**
-includes data cleaning, outlier handling, log transformations, and visualization of key relationships between exoplanet and star properties.

### **WorkFlow**
### 1️⃣ Handling Limit-Flagged Values
✅ Limit-Flagged Values:
    - Found 35 columns containing limit-flagged values **(e.g., <, >, min, max, etc.)**.
    ✅ set to **NaN** to ensure they do not interfere with numerical analysis.

### 2️⃣ Outlier Handling
-using a multi-method approach **IQR, Modified Z-score, and RobustScaler** for detection.
-Applied **winsorization** to handle extreme values while preserving integrity.

### 3️⃣ Log Transformations
- applied to columns with highly skewed distributions. 
  🚀 All transformations retained 45,975 valid values per column.

### 4️⃣ Key relationships and Correlation Analaysis
  ### 1️⃣ Star Mass vs. Planet Orbital Period
  -**Spearman ρ**: 0.086
  -**p-value**: 4.16e-76
  -**Sample Size (n)**: 45,975
  -**Interpretation**: Weak positive correlation. Higher star mass is slightly associated with longer planet orbital periods.

  ### 2️⃣ Planet Radius vs. Planet Mass
  -**Spearman ρ**: 0.058
  -**p-value**: 9.08e-36
  -**Sample Size (n)**: 45,975
  -**Interpretation**: Very weak positive correlation. Larger planets tend to have slightly higher masses, but the relationship is not strong.

  ### 3️⃣ Semi-Major Axis vs. Equilibrium Temperature
  -**Spearman ρ**: -0.510
  -**p-value**: 0.00e+00
  -**Sample Size (n)**: 45,975
  -**Interpretation**: Moderate negative correlation. Planets with smaller semi-major axes (closer to their stars) tend to have higher equilibrium temperatures.

  ### 4️⃣ Star Temperature vs. Planet Radius
  -**Spearman ρ**: 0.118
  -**p-value**: 1.88e-141
  -**Sample Size (n)**: 45,975
  -**Interpretation**: Weak positive correlation. Hotter stars tend to host slightly larger planets.

  ### 5️⃣ Semi-Major Axis vs. Equilibrium Temperature
  -**Spearman ρ**: 0.735
  -**p-value**: 0.00e+00
  -**Sample Size (n)**: 45,975
  -**Interpretation**: Strong positive correlation. Higher insolation flux (energy received from the star) is strongly associated with higher equilibrium temperatures.

### 5️⃣ Visualizations
✅ **Scatter Plots** with density coloring to highlight regions of high data concentration.  
✅ **Regression Lines** to visualize trends. 
✅ **Log scales** represent skewed data
