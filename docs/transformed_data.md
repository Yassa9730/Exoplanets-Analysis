# Log Transformation Report

## Overview
This report documents the application of log transformations to specific columns in the dataset to handle highly skewed data.

### **Columns Transformed**
The following columns were identified as highly skewed and underwent log transformation:
- `planet_period_x`
- `semi_major_axis_x`
- `pl_bmasse`
- `planet_radius_x`
- `pl_insol`

---

## Methodology
- **Log transformation** was applied to reduce skewness in the selected columns.
- Histograms and Q-Q plots were generated for both original and transformed data to visualize the impact.

### **Visual Analysis**
- **Histograms**: Showed a more normal-like distribution after transformation.
- **Q-Q Plots**: Indicated reduced deviation from normality.

---

## Skewness Comparison
| Column              | Original Skewness | Transformed Skewness |
|---------------------|-------------------|----------------------|
| planet_period_x     | 6.7490            | 1.2837               |
| semi_major_axis_x   | 5.3858            | 1.9702               |
| pl_bmasse           | 6.2162            | -2.1796              |
| planet_radius_x     | 3.2492            | 1.5200               |
| pl_insol            | 4.8462            | -0.5637              |
---

## Conclusion
- The log transformation **effectively reduced skewness**, improving data normality.
- The transformed data is now more suitable for statistical analysis and machine learning models.

The dataset is now better prepared for further processing and modeling.
