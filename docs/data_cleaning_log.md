### **Data Exploration and Initial Observations**
-**Data:** 2/11/2025
-**Dataset:** `nasa_exoplanets.csv`
-**Rows:** 38,063
-**Columns:** 92
-**Observations:**
    - Several columns have missing values (`pl_orbsmax`,, `st_spectype`, etc.).
    - The dataset contains metadata, wihch we handled by skippnig 96 rows.
    - Data types are a mix of `float64`, `int64`, and `object`. 
    