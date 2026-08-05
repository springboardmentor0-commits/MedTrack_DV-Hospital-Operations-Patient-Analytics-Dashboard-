import pandas as pd
import numpy as np

# ===========================
# Load Cleaned Dataset
# ===========================

df = pd.read_csv("hospital_cleaned.csv")

print("Hospital Dataset Loaded Successfully")
print(df.head())

# ===========================
# Convert Date Columns
# ===========================

df['Admission Date'] = pd.to_datetime(df['Admission Date'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

# ===========================
# KPI 1 - Total Admissions
# ===========================

total_admissions = df['Patient ID'].count()

# ===========================
# KPI 2 - Occupancy Rate
# ===========================

occupied_beds = len(df[df['Bed Status'] == 'Occupied'])
total_beds = len(df)

occupancy_rate = (occupied_beds / total_beds) * 100

# ===========================
# KPI 3 - Average Length of Stay
# ===========================

alos = df['Length of Stay (days)'].mean()

# ===========================
# KPI 4 - Readmission Rate
# ===========================

readmitted = len(df[df['Re-admission Flag'] == 'Yes'])

readmission_rate = (readmitted / total_admissions) * 100

# ===========================
# KPI 5 - Bed Utilization
# ===========================

bed_utilization = df.groupby('Ward')['Patient ID'].count().reset_index()

bed_utilization.columns = ['Ward', 'Patients']

# ===========================
# KPI 6 - Department Efficiency
# ===========================

department_efficiency = df.groupby('Department')['Patient ID'].count().reset_index()

department_efficiency.columns = ['Department', 'Patients']

# ===========================
# Monthly Admission Trend
# ===========================

df['Month'] = df['Admission Date'].dt.month_name()

monthly_admission = df.groupby('Month')['Patient ID'].count().reset_index()

monthly_admission.columns = ['Month', 'Admissions']

# ===========================
# Monthly Occupancy Trend
# ===========================

monthly_occupancy = df.groupby('Month')['Bed Status'].apply(
    lambda x: (x == 'Occupied').sum() / len(x) * 100
).reset_index()

monthly_occupancy.columns = ['Month', 'Occupancy Rate']

# ===========================
# Monthly Readmission Trend
# ===========================

monthly_readmission = df.groupby('Month')['Re-admission Flag'].apply(
    lambda x: (x == 'Yes').sum() / len(x) * 100
).reset_index()

monthly_readmission.columns = ['Month', 'Readmission Rate']

# ===========================
# KPI Summary
# ===========================

kpi_summary = pd.DataFrame({

    'KPI': [

        'Total Admissions',
        'Occupancy Rate',
        'Average Length of Stay',
        'Readmission Rate'

    ],

    'Value': [

        total_admissions,
        round(occupancy_rate,2),
        round(alos,2),
        round(readmission_rate,2)

    ]

})

# ===========================
# Export to Excel
# ===========================

with pd.ExcelWriter("hospital_final_dataset.xlsx") as writer:

    df.to_excel(writer,
                sheet_name="Cleaned Data",
                index=False)

    kpi_summary.to_excel(writer,
                         sheet_name="KPI Summary",
                         index=False)

    monthly_admission.to_excel(writer,
                               sheet_name="Monthly Admission",
                               index=False)

    monthly_occupancy.to_excel(writer,
                               sheet_name="Occupancy Trend",
                               index=False)

    monthly_readmission.to_excel(writer,
                                 sheet_name="Readmission Trend",
                                 index=False)

    department_efficiency.to_excel(writer,
                                   sheet_name="Department Analytics",
                                   index=False)

    bed_utilization.to_excel(writer,
                             sheet_name="Resource Utilization",
                             index=False)

print("===================================")
print("Hospital KPI Engineering Completed")
print("===================================")

print("Total Admissions :", total_admissions)
print("Occupancy Rate :", round(occupancy_rate,2), "%")
print("Average Length of Stay :", round(alos,2), "Days")
print("Readmission Rate :", round(readmission_rate,2), "%")

print("\nExcel File Created Successfully")
print("hospital_final_dataset.xlsx")
