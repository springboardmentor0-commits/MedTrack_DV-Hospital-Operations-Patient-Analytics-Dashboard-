import pandas as pd
import os

# Path to raw dataset
file_path = os.path.join(
    "data",
    "raw",
    "hospital_raw_data.csv"
)

# Load dataset
df = pd.read_csv(file_path)

print("=" * 50)
print("MEDTRACK DV - DATA COLLECTION")
print("=" * 50)

print("\nDataset loaded successfully!")

print("\nDataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFirst 5 Records:")
print(df.head())

print("\nColumn Names:")
for column in df.columns:
    print(column)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Calculate completeness
total_cells = df.shape[0] * df.shape[1]
missing_cells = df.isnull().sum().sum()

completeness = ((total_cells - missing_cells) / total_cells) * 100

print(f"\nDataset Completeness: {completeness:.2f}%")

if completeness > 95:
    print("Milestone Requirement: PASSED")
else:
    print("Milestone Requirement: NOT PASSED")

print("\nData collection completed successfully!")