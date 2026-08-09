# ==========================================================
# MedTrack DV
# Module 3 : Hospital KPI Engineering
# File : generate_hospital_kpis.py
# ==========================================================

import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Load Final Dataset
# ----------------------------------------------------------

hospital_final = pd.read_excel(
    "data/02_processed_data/hospital_final_dataset.xlsx"
)

print("Hospital Final Dataset Loaded Successfully.\n")

# ----------------------------------------------------------
# KPI 1 : Total Admissions
# ----------------------------------------------------------

total_admissions = hospital_final["Admission_ID"].nunique()

# ----------------------------------------------------------
# KPI 2 : Occupancy Rate
# ----------------------------------------------------------

occupied_beds = (hospital_final["Occupancy_Flag"] == 1).sum()

total_beds = hospital_final["Bed_ID"].nunique()

occupancy_rate = (occupied_beds / total_beds) * 100

# ----------------------------------------------------------
# KPI 3 : Average Length of Stay (ALOS)
# ----------------------------------------------------------

alos = hospital_final["Length_of_Stay"].mean()

# ----------------------------------------------------------
# KPI 4 : Readmission Rate
# ----------------------------------------------------------

readmission_rate = "Not Applicable"

# ----------------------------------------------------------
# KPI 5 : Bed Utilization Rate
# ----------------------------------------------------------

bed_utilization_rate = (
    (hospital_final["Bed_Status"] == "Occupied").sum()
    / hospital_final["Bed_ID"].nunique()
) * 100

# ----------------------------------------------------------
# KPI 6 : Department Efficiency Score
# ----------------------------------------------------------

department_efficiency = (
    hospital_final
    .groupby("Department_Name")
    .agg(
        Total_Admissions=("Admission_ID", "count"),
        Average_LOS=("Length_of_Stay", "mean")
    )
    .reset_index()
)

department_efficiency["Efficiency_Score"] = (
    department_efficiency["Total_Admissions"]
    / department_efficiency["Average_LOS"]
).round(2)

average_efficiency = department_efficiency[
    "Efficiency_Score"
].mean()

#----------------------------------------------------------
# Additional KPI : Total Revenue
# ----------------------------------------------------------

total_revenue = hospital_final["Total"].sum()

# ----------------------------------------------------------
# KPI Summary
# ----------------------------------------------------------

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Admissions",
        "Occupancy Rate (%)",
        "Average Length of Stay (Days)",
        "Readmission Rate",
        "Bed Utilization Rate (%)",
        "Department Efficiency Score",
        "Total Revenue"
    ],
    "Value": [
        total_admissions,
        round(occupancy_rate, 2),
        round(alos, 2),
        readmission_rate,
        round(bed_utilization_rate, 2),
        round(average_efficiency, 2),
        round(total_revenue, 2)
    ]
})

# ----------------------------------------------------------
# Display KPI Summary
# ----------------------------------------------------------

print("=" * 50)
print("Hospital KPI Summary")
print("=" * 50)

print(kpi_summary)

# ----------------------------------------------------------
# Save KPI Summary
# ----------------------------------------------------------

kpi_summary.to_excel(
    "data/02_processed_data/hospital_kpi_summary.xlsx",
    index=False
)

print("\nHospital KPI Summary exported successfully.")