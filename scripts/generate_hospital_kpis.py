from pathlib import Path
import pandas as pd
import numpy as np

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Cleaned dataset
file_path = BASE_DIR / "data" / "processed" / "hospital_cleaned.csv"

# Load dataset
df = pd.read_csv(file_path)

# Convert date columns
df["Admission Date"] = pd.to_datetime(df["Admission Date"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

print("✅ Cleaned dataset loaded successfully!")
print("Shape:", df.shape)

# KPI 1: Total Admissions
total_admissions = df["Patient ID"].nunique()

print("\nTotal Admissions:", total_admissions)

# KPI 2: Occupancy Rate
total_beds = len(df)
occupied_beds = (df["Bed Status"] == "Occupied").sum()

occupancy_rate = (occupied_beds / total_beds) * 100

print("Occupancy Rate:", round(occupancy_rate, 2), "%")

# KPI 3: Average Length of Stay (ALOS)
alos = df["Length of Stay (days)"].mean()

print("Average Length of Stay (ALOS):", round(alos, 2), "days")

# KPI 4: Readmission Rate
readmitted_patients = (df["Re-admission Flag"] == "Yes").sum()
readmission_rate = (readmitted_patients / total_admissions) * 100

print("Readmission Rate:", round(readmission_rate, 2), "%")

# KPI 5: Bed Utilization Rate
bed_utilization_rate = (
    df["Bed Status"].value_counts(normalize=True).get("Occupied", 0) * 100
)

print("Bed Utilization Rate:", round(bed_utilization_rate, 2), "%")

# KPI 6: Department Efficiency Score

department_stats = df.groupby("Department").agg(
    Admissions=("Patient ID", "count"),
    Avg_Length_of_Stay=("Length of Stay (days)", "mean")
)

department_stats["Efficiency Score"] = (
    department_stats["Admissions"] /
    department_stats["Avg_Length_of_Stay"]
)

print("\nDepartment Efficiency Score:")
print(department_stats[["Admissions", "Avg_Length_of_Stay", "Efficiency Score"]])

# -----------------------------------------
# Export Tableau-ready dataset
# -----------------------------------------

# Add KPI-related fields to the dataset
df["Total Admissions"] = total_admissions
df["Occupancy Rate (%)"] = occupancy_rate
df["Average Length of Stay (ALOS)"] = alos
df["Readmission Rate (%)"] = readmission_rate
df["Bed Utilization Rate (%)"] = bed_utilization_rate

# Add department efficiency score to each patient record
efficiency_map = department_stats["Efficiency Score"].to_dict()

df["Department Efficiency Score"] = df["Department"].map(efficiency_map)

# Output path
output_path = BASE_DIR / "data" / "processed" / "hospital_final_dataset.xlsx"

# Export to Excel
df.to_excel(output_path, index=False)

print("\n✅ Tableau-ready dataset exported successfully!")
print("Output file:", output_path)
print("Final shape:", df.shape)