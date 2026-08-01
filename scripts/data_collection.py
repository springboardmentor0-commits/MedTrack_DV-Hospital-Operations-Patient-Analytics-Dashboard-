import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_hospital_data(num_records=5000, seed=42):
    np.random.seed(seed)
    
    first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 
                   'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica', 
                   'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa', 
                   'Matthew', 'Betty', 'Anthony', 'Margaret', 'Donald', 'Sandra', 'Mark', 'Ashley', 
                   'Paul', 'Kimberly', 'Steven', 'Emily', 'Andrew', 'Donna', 'Kenneth', 'Michelle']
    
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 
                  'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 
                  'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 
                  'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker']
    
    hospitals_regions = [
        ('City Care Hospital', 'North'),
        ('Green Valley Hospital', 'South'),
        ('Sunrise Medical Center', 'East'),
        ('Metro Health Institute', 'West'),
        ('HealthPlus Hospital', 'Central')
    ]
    
    departments = ['General Medicine', 'Surgery', 'Pediatrics', 'Orthopedics', 'Cardiology', 'Emergency', 'ICU']
    dept_variations = departments + ['cardiology', 'ICU ', 'Pediatrics ', 'general medicine', 'SURGERY']
    
    patient_types = ['Inpatient', 'Outpatient', 'Emergency', 'Day Care']
    admission_types = ['Emergency', 'Urgent', 'Elective']
    severities = ['Low', 'Moderate', 'High', 'Critical']
    equipment_list = ['Ventilator', 'MRI Scanner', 'CT Scanner', 'Ultrasound', 'X-Ray Machine', 'None']
    
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range_days = (end_date - start_date).days
    
    records = []
    
    for i in range(1, num_records + 1):
        pat_id = f"PAT-{10000 + i}"
        name = f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        age = int(np.random.randint(1, 90))
        gender = np.random.choice(['Male', 'Female', 'Other'], p=[0.48, 0.49, 0.03])
        
        hosp, region = hospitals_regions[np.random.choice(len(hospitals_regions))]
        dept = np.random.choice(dept_variations)
        pat_type = np.random.choice(patient_types, p=[0.45, 0.30, 0.15, 0.10])
        adm_type = np.random.choice(admission_types, p=[0.40, 0.35, 0.25])
        severity = np.random.choice(severities, p=[0.30, 0.40, 0.20, 0.10])
        
        random_days = np.random.randint(0, date_range_days)
        adm_date = start_date + timedelta(days=int(random_days))
        
        # Length of stay depends on severity and dept
        if severity == 'Critical':
            los = int(np.random.randint(5, 25))
        elif severity == 'High':
            los = int(np.random.randint(3, 14))
        elif severity == 'Moderate':
            los = int(np.random.randint(1, 7))
        else:
            los = int(np.random.randint(1, 4))
            
        dis_date = adm_date + timedelta(days=los)
        
        # Readmission chance higher for critical/high
        readmitted_prob = 0.25 if severity in ['High', 'Critical'] else 0.08
        readmitted = 'Yes' if np.random.random() < readmitted_prob else 'No'
        
        bed_utilization = round(float(np.random.uniform(65.0, 98.5)), 2)
        staff_assigned = int(np.random.randint(1, 6))
        equipment = np.random.choice(equipment_list)
        treatment_cost = round(float(los * np.random.uniform(300, 1200) + np.random.uniform(200, 1500)), 2)
        satisfaction_score = round(float(np.random.uniform(1.0, 5.0)), 1)
        
        record = {
            'Patient_ID': pat_id,
            'Patient_Name': name,
            'Age': age,
            'Gender': gender,
            'Hospital_Name': hosp,
            'Region': region,
            'Department': dept,
            'Patient_Type': pat_type,
            'Admission_Type': adm_type,
            'Severity': severity,
            'Admission_Date': adm_date.strftime('%Y-%m-%d'),
            'Discharge_Date': dis_date.strftime('%Y-%m-%d'),
            'Length_of_Stay': los,
            'Readmitted_30_Days': readmitted,
            'Bed_Utilization_Pct': bed_utilization,
            'Staff_Assigned': staff_assigned,
            'Equipment_Used': equipment,
            'Treatment_Cost': treatment_cost,
            'Satisfaction_Score': satisfaction_score
        }
        records.append(record)
        
    df = pd.DataFrame(records)
    
    # Introduce ~1.5% duplicates
    num_duplicates = int(num_records * 0.015)
    dup_indices = np.random.choice(df.index, size=num_duplicates, replace=False)
    duplicates = df.loc[dup_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Introduce ~2.5% missing values randomly in non-critical columns to evaluate data cleaning step
    for col in ['Discharge_Date', 'Satisfaction_Score', 'Equipment_Used', 'Readmitted_30_Days']:
        mask = np.random.random(len(df)) < 0.025
        df.loc[mask, col] = np.nan
        
    return df

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(project_dir, 'data')
    
    os.makedirs(data_dir, exist_ok=True)
    
    df_raw = generate_hospital_data(num_records=5000)
    
    raw_path_data = os.path.join(data_dir, 'hospital_raw_data.csv')
    raw_path_root = os.path.join(project_dir, 'hospital_raw_data.csv')
    
    df_raw.to_csv(raw_path_data, index=False)
    df_raw.to_csv(raw_path_root, index=False)
    
    non_null_pct = (1 - df_raw.isnull().sum().sum() / df_raw.size) * 100
    print(f"Generated raw dataset with {len(df_raw)} records.")
    print(f"Dataset completeness: {non_null_pct:.2f}% (Target > 95%)")
    print(f"Saved raw data to {raw_path_data} and {raw_path_root}")
