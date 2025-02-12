### **Data Exploration and Initial Observations**
- **Date:** 2/11/2025  
- **Dataset:** `nasa_exoplanets.csv`  
- **Rows:** 38,063  
- **Columns:** 92  

#### **Observations**
- Several columns have missing values (`pl_orbsmax`, `st_spectype`, etc.).
- The dataset contained metadata, which we handled by **skipping 96 rows**.
- Data types include `float64`, `int64`, and `object`.

---

### **Missing Value Handling**
✅ Dropped columns with more than **50% missing values**.  
✅ Filled numeric columns with the **median**.  
✅ Filled categorical columns with `"unknown"`.

---

### **EDA Insights**
#### **Exoplanet Discoveries**
- Discoveries peaked in **2016**, followed closely by **2014**.
- Both years had significantly higher discovery counts compared to other years, possibly due to advancements in space observation technologies.

#### **Correlation Between Planet Size and Mass**
- There is **no strong correlation** between planet radius and mass.
- Most planets fall within the range of **0 to 10 Jupiter masses** and **1 to 2 Jupiter radii**, suggesting a concentration of typical gas giant planets.

---

## **Data Cleaning Log**
- **Dataset:** `exoplanet_eu_data.csv`  
- **Cleaned Version:** `exoplanet_eu_cleaned.csv`  
- **Date:** 2/12/2025  
- **Author:** Yassa  

### **1. Issues in the Original Dataset**
- The first **101 rows** contained metadata instead of actual data.
- Some columns had **more than 50% missing values**.
- Numeric columns had missing values that needed **imputation**.
- Categorical columns had missing values that needed **filling**.

### **2. Cleaning Steps Performed**
✅ **Skipped metadata rows** (`skiprows=101`).  
✅ **Checked missing values** before cleaning.  
✅ **Dropped columns** with more than **50% missing values**.  
✅ **Filled missing numeric values** using the **median** to avoid outliers.  
✅ **Filled missing categorical values** with `"unknown"`.  
✅ **Checked missing values again** to verify cleaning was successful.  
✅ **Saved the cleaned dataset** as `exoplanet_eu_cleaned.csv`.  

---

### **3. Results After Cleaning**
- The dataset is now **ready for merging** with other exoplanet datasets.  
- No critical missing values remain.  
- The cleaned file is stored in the `data/` directory.  

---

### **4. Next Steps**
- **Merge** this dataset with `nasa_exoplanets_cleaned.csv` and `exoplanet.csv`.  
- **Perform exploratory data analysis (EDA)** on the combined dataset.  


## **NASA Exoplanet Data Cleaning**
- **Dataaset:** `nasa_exoplanets_cleaned.csv`
- **Cleaned Version:** `nasa_exoplanets_cleaned.csv`
- **Date:** 2/12/2025
- **Author:** Yassa

### **1. Issues in the original Dataset**
- The first **96 rows** contained metadata instead of actuaal data.


### **2.Cleaning Steps Performed**
✅ **Skipped metadata rows** *`skiprows=96`).
✅ **Verified first rows to ensure correct formatting**.
✅ **Saved cleaned dataset as `nassa_exoplanets_cleaned.csv`**.


### **3.Next Steps**
- Clean exoplanet.csv Before Merging

