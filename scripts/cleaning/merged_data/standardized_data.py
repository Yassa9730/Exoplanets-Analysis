import pandas as pd

# Load dataset safely
df = pd.read_csv(r"C:\CS50 Final Project\data\merged_exoplanets_final.csv")

# Debugging: Print column names
print("Existing Columns:", df.columns.tolist())

# Fix incorrect column name (typo)
if "discovey_year" in df.columns:
    df.rename(columns={"discovey_year": "discovery_year"}, inplace=True)

# Remove unnecessary columns safely
columns_to_drop = ["default_flag", "pl_controv_flag", "pl_refname", "st_refname", "sy_refname",
                   "rowupdate", "pl_pubdate", "releasedate"]
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# Standardize missing values for categorical columns
df.fillna({"discovery_method": "Unknown", "disc_facility": "Unknown"}, inplace=True)

# Fix discovery year column
if "discovery_year" in df.columns:
    df["discovery_year"] = df["discovery_year"].fillna(0).astype(int)

# Ensure `is_transiting` is always 0 or 1
if "is_transiting" in df.columns:
    df["is_transiting"] = pd.to_numeric(df["is_transiting"], errors="coerce").fillna(0).astype(int)

# Fix spelling errors in dataset
df.replace(["unknown", "unkown", "UNKNOWN"], "Unknown", inplace=True)

# Fill missing mass values using available data
if "pl_bmasse" in df.columns and "pl_bmassj" in df.columns:
    df["pl_bmassj"] = df["pl_bmassj"].fillna(df["pl_bmasse"] * 0.00315)
    df["pl_bmasse"] = df["pl_bmasse"].fillna(df["pl_bmassj"] * 317.8)

# Also fill general `mass` column if missing
if "mass" in df.columns and "pl_bmassj" in df.columns and "pl_bmasse" in df.columns:
    df["mass"] = df["mass"].fillna(df["pl_bmassj"])
    df["mass"] = df["mass"].fillna(df["pl_bmasse"] * 0.00315)


# Convert numeric columns safely
numeric_columns = ["pl_bmasse", "pl_bmassj", "star_mass", "star_radius", "planet_radius"]
missing_columns = [col for col in numeric_columns if col not in df.columns]
if missing_columns:
    print("⚠ Warning: These columns are missing and won't be converted:", missing_columns)

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned dataset safely
df.to_csv(r"C:\CS50 Final Project\data\merged_exoplanets_standardized.csv", index=False, encoding="utf-8")

print("✅ Data cleaning and standardization complete!")
