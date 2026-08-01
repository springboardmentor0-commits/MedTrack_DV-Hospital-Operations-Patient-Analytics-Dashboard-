import os
import pandas as pd
import numpy as np

def calculate_kpis():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_path = os.path.join(project_dir, 'data', 'hospital_cleaned.csv')
    
    if not os.path.exists(cleaned_path):
        cleaned_path = os.path.join(project_dir, 'hospital_cleaned.csv')
        
    print(f"Reading cleaned dataset from: {cleaned_path}")
    df = pd.read_csv(cleaned_path)
    
    # Ensure date fields
    df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
    df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])
    df['Year_Month'] = df['Admission_Date'].dt.strftime('%Y-%m')
    df['Is_Readmitted'] = (df['Readmitted_30_Days'] == 'Yes').astype(int)
    
    # 1. Executive Summary KPIs
    total_admissions = len(df)
    occupancy_rate = df['Bed_Utilization_Pct'].mean()
    alos = df['Length_of_Stay'].mean()
    readmission_rate = (df['Is_Readmitted'].sum() / total_admissions) * 100
    bed_utilization_rate = df['Bed_Utilization_Pct'].mean()
    dept_efficiency_score = df['Dept_Efficiency_Score'].mean()
    
    summary_df = pd.DataFrame([{
        'Metric': 'Total Admissions', 'Value': total_admissions, 'Unit': 'Patients'
    }, {
        'Metric': 'Occupancy Rate', 'Value': round(occupancy_rate, 2), 'Unit': '%'
    }, {
        'Metric': 'Average Length of Stay (ALOS)', 'Value': round(alos, 2), 'Unit': 'Days'
    }, {
        'Metric': 'Readmission Rate (30-Day)', 'Value': round(readmission_rate, 2), 'Unit': '%'
    }, {
        'Metric': 'Bed Utilization Rate', 'Value': round(bed_utilization_rate, 2), 'Unit': '%'
    }, {
        'Metric': 'Department Efficiency Score', 'Value': round(dept_efficiency_score, 2), 'Unit': 'Score (0-100)'
    }])
    
    # 2. Department-level KPIs
    dept_kpis = df.groupby('Department').agg(
        Total_Admissions=('Patient_ID', 'count'),
        Avg_Length_of_Stay=('Length_of_Stay', lambda x: round(x.mean(), 2)),
        Readmission_Rate_Pct=('Is_Readmitted', lambda x: round((x.sum() / len(x)) * 100, 2)),
        Avg_Bed_Utilization_Pct=('Bed_Utilization_Pct', lambda x: round(x.mean(), 2)),
        Avg_Treatment_Cost=('Treatment_Cost', lambda x: round(x.mean(), 2)),
        Avg_Satisfaction_Score=('Satisfaction_Score', lambda x: round(x.mean(), 2)),
        Dept_Efficiency_Score=('Dept_Efficiency_Score', lambda x: round(x.mean(), 2))
    ).reset_index()
    
    # 3. Monthly Operational Trends
    monthly_kpis = df.groupby('Year_Month').agg(
        Admissions=('Patient_ID', 'count'),
        Avg_Occupancy_Pct=('Bed_Utilization_Pct', lambda x: round(x.mean(), 2)),
        Avg_Length_of_Stay=('Length_of_Stay', lambda x: round(x.mean(), 2)),
        Readmission_Rate_Pct=('Is_Readmitted', lambda x: round((x.sum() / len(x)) * 100, 2)),
        Total_Treatment_Cost=('Treatment_Cost', lambda x: round(x.sum(), 2))
    ).reset_index()
    
    # 4. Hospital & Region KPIs
    hosp_kpis = df.groupby(['Hospital_Name', 'Region']).agg(
        Total_Admissions=('Patient_ID', 'count'),
        Avg_Occupancy_Pct=('Bed_Utilization_Pct', lambda x: round(x.mean(), 2)),
        Avg_Length_of_Stay=('Length_of_Stay', lambda x: round(x.mean(), 2)),
        Readmission_Rate_Pct=('Is_Readmitted', lambda x: round((x.sum() / len(x)) * 100, 2)),
        Avg_Efficiency_Score=('Dept_Efficiency_Score', lambda x: round(x.mean(), 2))
    ).reset_index()
    
    # Write to Excel workbook
    output_excel_data = os.path.join(project_dir, 'data', 'hospital_final_dataset.xlsx')
    output_excel_root = os.path.join(project_dir, 'hospital_final_dataset.xlsx')
    
    with pd.ExcelWriter(output_excel_data, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Patient_Analytics', index=False)
        summary_df.to_excel(writer, sheet_name='Executive_KPI_Summary', index=False)
        dept_kpis.to_excel(writer, sheet_name='Department_Performance', index=False)
        monthly_kpis.to_excel(writer, sheet_name='Monthly_Operational_Trends', index=False)
        hosp_kpis.to_excel(writer, sheet_name='Hospital_Region_Summary', index=False)
        
    with pd.ExcelWriter(output_excel_root, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Patient_Analytics', index=False)
        summary_df.to_excel(writer, sheet_name='Executive_KPI_Summary', index=False)
        dept_kpis.to_excel(writer, sheet_name='Department_Performance', index=False)
        monthly_kpis.to_excel(writer, sheet_name='Monthly_Operational_Trends', index=False)
        hosp_kpis.to_excel(writer, sheet_name='Hospital_Region_Summary', index=False)
        
    print(f"Successfully generated hospital KPIs and saved final Excel workbook to '{output_excel_data}' and '{output_excel_root}'.")
    print("\n--- KPI Summary ---")
    print(summary_df.to_string(index=False))

if __name__ == '__main__':
    calculate_kpis()
