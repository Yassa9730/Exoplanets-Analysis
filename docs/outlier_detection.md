### **Outlier Detection And Handling Limit-Flagged Values**

### **Cleaning Limit-Flagged Values**
The clean_limit_values function is designed to identify and clean columns that may contain limit-flagged values (e.g., values prefixed with < or >). These values are often used to indicate that a measurement is below or above a certain threshold but are not directly usable in numerical analysis.

✅ Identify columns with Limit Flags **max, min, upper, lower, lim, ul, ll, constraint, bound, <, or >.**.  
✅ Clean Limit-Flageed values **replaces string values like <0.5 or >10 with NaN**.  


#### **Detecting Outliers Using IQR Method**
✅ **Calculate IQR** (`IQR=Q3-Q1`).  
✅ **Determine Outlier Bounds** lower bound **Q1-1.5xIQR** , upper bound **Q3+1.5xIQR**
✅ **Identify Outliers** 
✅ **Visualization** using **Box Plots** 
✅ **Output** no, of outliers, upper and lower bound, sample outliers(if any)

#### **WorkFlow**
✅ **Clean limit values**   
✅ **Identify numerical columns** using **df.select_dtypes(include=['float64'])** 
✅ **Detect Outliers** 
✅ **Review And Analyze** 
