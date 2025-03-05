#used 3.11.6 version

import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
file_path = "updated_exoplanets.csv"  
df = pd.read_csv(file_path)

# Handle extreme values (optional)
# df = df[df.select_dtypes(include=['number']).apply(lambda x: (x < 1e6).all(), axis=1)]  # Filter extreme numbers

# Limit profiling settings to reduce memory usage
profile = ProfileReport(df, explorative=True, minimal=True, samples=None)

profile.to_file("updated_exoplanets.html")
