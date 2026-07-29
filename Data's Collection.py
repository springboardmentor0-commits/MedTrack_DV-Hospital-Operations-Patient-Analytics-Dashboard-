import pandas as pd
import os

# ----------------------------
# Hospital Data Collection
# ----------------------------

FILE_NAME = "hospital_raw_data.csv"

# Check if dataset exists
if not os.path.exists(FILE_NAME):
    print(f"Error: {FILE_NAME} not found.")
    exit()

# Load dataset
df = pd.read_csv(FILE_NAME)

print("=" * 50)
print("MEDTRACK DV - DATA COLLECTION")
print("=" * 50)

# Dataset Information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Records
duplicates = df.duplicated().sum()
print("\nDuplicate Records:", duplicates)

# Dataset Completeness
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()
completeness = ((total_cells - missing_cells) / total_cells) * 100

print(f"\nDataset Completeness: {completeness:.2f}%")

# Save Dataset
df.to_csv("hospital_raw_data.csv", index=False)

print("\nData Collection Completed Successfully!")
print("Output File: hospital_raw_data.csv")
