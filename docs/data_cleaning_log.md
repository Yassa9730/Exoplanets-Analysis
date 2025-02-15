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


## **Exooplanet Data Cleaning**
- **Dataset:** `eexoplanets.csv`
- **Cleaned Version:** `exoplanets_cleaned.csv`
- **Date:** 2/12/2025
- **Author:** Yassa


### **1. Issues in the Origin Dataset**
 - The first **21 rows** contained metadata instead of actuaal data.
 - Some columns had missing values, **but none exceeded 50%**, so all columns were retained.
 - Numeric columns had missing values that needed **imputation**
 - Categorical columns had missing values that needed **filling**.


### **2. Cleaning Steps Performed**
✅ **Checked for and remmoved metadata rows**.
✅ **Filled missing numeric Values** with the **median**
✅ **Filled missing categorical values** with `"unkown"`
✅ **Saved cleaned dataset as `exoplanets_cleaned.csv`**.


### **3. Next Steps**
- Merge `exoplanets_cleaned.csv` with `nasa_exoplanets_cleaned.csv` and `exoplanet_eu_data.csv`.

## **5. Dataset Merging**
### **Merged Version:** `merged_exoplanets.csv`
### **Date:** 2/13/2025
### **Author:** Yassa

#### **1️⃣ Merging Process**
✅ Combined three cleaned datasets:
    - `nasa_exolanets_cleaned.csv`
      - `exoplanet_eu_data.csv`
      - `exoplanets_cleaned.csv`
✅Used **outer Join** on `planet_name`, `star_name`, and `discovery_year`
✅ Preserved all available data while avoiding duplicate entries

#### **2️⃣ Issues Noted**
📌 Some columns contained missing values due to differences in available data across datasets.
📌 The **citation fields** in NASA data still contain HTML references (e.g., `<a refstr=...>`), which will be cleaned next.


#### **2️⃣ Next Steps**
👉 Extract author names & years from citation fields.
👉 Remove unnecessary HTML tags while keeping useful citation info.
👉 Verify final dataset integrity before anlysis

## **6. Cleaning Citations in References**
- **Columns Cleaned:** `pl_refname`, `st_refname`, `sy_refname`
- **Issue:** These columns contained HTML `<a>` tags with links.
- **Solution:** We extracted only the **author name & year**, removing extra formatting.
- **Example Fix:**
  - Before: `<a refstr=KUNITOMO_ET_AL__2011 href=...>Kunitomo et al. 2011</a>`
  - After: `Kunitomo et al. 2011`
- **Result:** The dataset now contains **clean citations** for better readability.


# Cleaning Log: Merged Exoplanets Dataset
** Dataset:** `merged_exoplanets_final.csv`
**Date:** 2/15/2025
**Author:** Yassa

## 6️⃣ Cleaning & Verification of Merged Dataset

### 1️⃣ Cleaning Steps
✅ Handled missing values:
    - Filleed numeric columns with **median**.
    - Filled categorical columns wiht **"unknown"**.
  ✅ Droped **5 columns** with more than **90%% missing data**.
  ✅ Verified final dataset strcuture (**133 columns**)

  ### 2️⃣ Verification
  ✅ Ran `info()` to confirm **correct data types**
  ✅ Used `describe()` to ensure **numerical values are within expected ranges**.

  ### 3️⃣ Next Steps
  🚀 The dataset is **now cleaner but not final**. Further column adjustments and standardizations are before **EDA**

