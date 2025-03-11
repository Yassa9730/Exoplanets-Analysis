# **Data Exploration and Cleaning Log**

## **1️⃣ Data Exploration and Initial Observations**
- **Date:** 2/11/2025  
- **Dataset:** `nasa_exoplanets.csv`  
- **Rows:** 38,063  
- **Columns:** 92  

### **Observations**
- Several columns have missing values (`pl_orbsmax`, `st_spectype`, etc.).
- The dataset contained metadata, which we handled by **skipping 96 rows**.
- Data types include `float64`, `int64`, and `object`.

---

## **2️⃣ Missing Value Handling**
✅ Dropped columns with more than **50% missing values**.  
✅ Filled numeric columns with the **median**.  
✅ Filled categorical columns with `"unknown"`.

---

## **3️⃣ Exploratory Data Analysis (EDA) Insights**
### **Exoplanet Discoveries**
- Discoveries peaked in **2016**, followed closely by **2014**.
- Both years had significantly higher discovery counts compared to other years, possibly due to advancements in space observation technologies.

### **Correlation Between Planet Size and Mass**
- There is **no strong correlation** between planet radius and mass.
- Most planets fall within the range of **0 to 10 Jupiter masses** and **1 to 2 Jupiter radii**, suggesting a concentration of typical gas giant planets.

---

# **4️⃣ Data Cleaning Logs**
## **NASA Exoplanet Data Cleaning**
- **Dataset:** `nasa_exoplanets_cleaned.csv`
- **Cleaned Version:** `nasa_exoplanets_cleaned.csv`
- **Date:** 2/12/2025
- **Author:** Yassa

### **1. Issues in the Original Dataset**
- The first **96 rows** contained metadata instead of actual data.

### **2. Cleaning Steps Performed**
✅ **Skipped metadata rows** (`skiprows=96`).  
✅ **Verified first rows to ensure correct formatting**.  
✅ **Saved cleaned dataset as `nasa_exoplanets_cleaned.csv`**.

### **3. Next Steps**
- Clean `exoplanets.csv` before merging.

---

## **Exoplanet Data Cleaning**
- **Dataset:** `exoplanets.csv`
- **Cleaned Version:** `exoplanets_cleaned.csv`
- **Date:** 2/12/2025  
- **Author:** Yassa  

### **1. Issues in the Original Dataset**
- The first **21 rows** contained metadata instead of actual data.
- Some columns had missing values, **but none exceeded 50%**, so all columns were retained.
- Numeric columns had missing values that needed **imputation**.
- Categorical columns had missing values that needed **filling**.

### **2. Cleaning Steps Performed**
✅ **Checked for and removed metadata rows**.  
✅ **Filled missing numeric values** with the **median**.  
✅ **Filled missing categorical values** with `"unknown"`.  
✅ **Saved cleaned dataset as `exoplanets_cleaned.csv`**.  

### **3. Next Steps**
- Merge `exoplanets_cleaned.csv` with `nasa_exoplanets_cleaned.csv` and `exoplanet_eu_data.csv`.

---

## **5️⃣ Dataset Merging**
- **Merged Version:** `merged_exoplanets.csv`
- **Date:** 2/13/2025
- **Author:** Yassa

### **1. Merging Process**
✅ Combined three cleaned datasets:
   - `nasa_exoplanets_cleaned.csv`
   - `exoplanet_eu_data.csv`
   - `exoplanets_cleaned.csv`
✅ Used **outer join** on `planet_name`, `star_name`, and `discovery_year`.  
✅ Preserved all available data while avoiding duplicate entries.

### **2. Issues Noted**
📌 Some columns contained missing values due to differences in available data across datasets.  
📌 The **citation fields** in NASA data still contain HTML references (e.g., `<a refstr=...>`), which will be cleaned next.

### **3. Next Steps**
👉 Extract author names & years from citation fields.  
👉 Remove unnecessary HTML tags while keeping useful citation info.  
👉 Verify final dataset integrity before analysis.  

---

## **6️⃣ Cleaning Citations in References**
- **Columns Cleaned:** `pl_refname`, `st_refname`, `sy_refname`
- **Issue:** These columns contained HTML `<a>` tags with links.
- **Solution:** We extracted only the **author name & year**, removing extra formatting.
- **Example Fix:**
  - **Before:** `<a refstr=KUNITOMO_ET_AL__2011 href=...>Kunitomo et al. 2011</a>`
  - **After:** `Kunitomo et al. 2011`
- **Result:** The dataset now contains **clean citations** for better readability.

---

# **7️⃣ Cleaning Log: Merged Exoplanets Dataset**
- **Dataset:** `merged_exoplanets_final.csv`
- **Date:** 2/15/2025
- **Author:** Yassa

### **1. Cleaning & Verification of Merged Dataset**
✅ Handled missing values:  
   - Filled numeric columns with **median**.  
   - Filled categorical columns with **"unknown"**.  
✅ Dropped **5 columns** with more than **90% missing data**.  
✅ Verified final dataset structure (**133 columns**).

### **2. Verification**
✅ Ran `df.info()` to confirm **correct data types**.  
✅ Used `df.describe()` to ensure **numerical values are within expected ranges**.

### **3. Next Steps**
🚀 The dataset is **now cleaner but not final**. Further column adjustments and standardizations are needed before **EDA**.


## 2/16/2025 - Standardized and Cleaned Exoplanet Dataset

### Changes:
- Fixed column names (_removed `_x` and `_y` suffixes_)
- Dropped unnecessary columns
- Filled missing values (_discovery method, mass, etc._)
- Standardized `discovery_year`, `is_transiting`, and other key fields
- Replaced misspellings (e.g., `unkown` → `Unknown`)
- Saved the cleaned dataset as `merged_exoplanets_standardized.csv`
