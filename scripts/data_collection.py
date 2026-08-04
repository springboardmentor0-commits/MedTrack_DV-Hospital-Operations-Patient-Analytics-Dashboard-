import pandas as pd

# Dataset path
file_path = "data/raw/CS_Healthcare_MediCare.xlsx.csv"

# Load dataset
df = pd.read_csv(file_path)

# Convert date columns
df["Admission Date"] = pd.to_datetime(df["Admission Date"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

print("✅ Dataset loaded successfully!\n")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())