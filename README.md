# MedTrack DV - Hospital Operations and Patient Analytics Dashboard

# Project Description

MedTrack DV is a hospital operations and patient analytics project developed to analyze hospital data and support better decision-making. The project involves data cleaning, integration, feature engineering, and the creation of master datasets for further analysis and dashboard development.

## Objectives

- Clean and preprocess hospital datasets
- Integrate multiple datasets into a single master dataset
- Create master datasets for different hospital operations
- Perform data analysis and KPI generation
- Build interactive Tableau dashboards

## Project Structure

```
MedTrack_DV-Hospital-Operations-Patient-Analytics-Dashboard/

├── data
│   ├── 01_raw_data
│   └── 02_processed_data
│
├── notebooks
│   ├── 01_milestone1_data_cleaning.ipynb
│   ├── 02_master_datasets.ipynb
│   └── 03_bed_master_generation.ipynb
│
├── docs
├── scripts
└── README.md
```

## Datasets Used

Raw Datasets

- Patients
- Admissions
- Doctors
- Departments
- Billing
- Surgeries
- Medications
- Lab Results

Processed Datasets

- patients_cleaned.csv
- admissions_cleaned.csv
- doctors_cleaned.csv
- departments_cleaned.csv
- billing_cleaned.csv
- surgeries_cleaned.csv
- medications_cleaned.csv
- lab_results_cleaned.csv

Master Datasets

- hospital_master_dataset.csv
- doctor_master.csv
- billing_master.csv
- bed_master.csv

## Technologies Used

- Python
- Pandas
- NumPy
- Faker
- Jupyter Notebook
- Tableau
- Git
- GitHub

## Workflow

1. Load raw datasets
2. Clean and preprocess the data
3. Perform feature engineering
4. Integrate datasets
5. Create hospital master dataset
6. Create doctor, billing and bed master datasets
7. Perform data analysis and KPI generation
8. Develop Tableau dashboards

## Current Progress

Completed:
- Data Cleaning
- Data Integration
- Feature Engineering
- Hospital Master Dataset
- Doctor Master Dataset
- Billing Master Dataset
- Bed Master Dataset

Next Steps:
- Exploratory Data Analysis (EDA)
- KPI Generation
- Tableau Dashboard Development


Milestone 2: KPI Engineering & Dashboard Planning
Overview

The second milestone focuses on transforming the cleaned hospital dataset into meaningful healthcare KPIs and developing an interactive Tableau dashboard prototype. The processed dataset was optimized for visualization, and healthcare metrics were calculated to support data-driven hospital management.


Module 3: Hospital KPI Engineering
Objectives
Calculate healthcare performance metrics.
Prepare a Tableau-ready dataset.
Automate KPI generation using Python.
KPIs Calculated
Total Admissions
Occupancy Rate
Average Length of Stay (ALOS)
Bed Utilization Rate
Department Efficiency Score
Total Revenue

Note:
Readmission Rate was not calculated because each patient has only one admission record in the dataset.

Files Created
scripts/
└── generate_hospital_kpis.py

data/
└── 02_processed_data/
    ├── hospital_final_dataset.xlsx
    └── hospital_kpi_summary.xlsx

    
Module 4: Dashboard Planning & Prototype
Objective

Design and develop interactive Tableau dashboards to visualize hospital operations and patient analytics.

Dashboards Developed
1. Hospital Overview

Includes:

Total Admissions
Occupancy Rate
Average Length of Stay
Total Revenue
Monthly Admissions Trend
Department-wise Admissions
Diagnosis Distribution
Department Revenue

2. Patient Flow

Includes:

Admissions by Day
Length of Stay Distribution
Stay Category Distribution
Age Group Distribution
Weekend vs Weekday Admissions
Admission Status

3. Department Analytics

Includes:

Department-wise Admissions
Department Revenue
Average Length of Stay by Department
Department Efficiency Comparison
Top Doctors by Admissions
Diagnosis Distribution by Department

4. Resource Utilization

Includes:

Bed Status Distribution
Ward-wise Bed Utilization
Bed Type Distribution
Floor-wise Occupancy
Department-wise Bed Usage
Occupancy by Bed Type

Interactive Features
Dashboard Filters
Cross-dashboard Filter Actions
Department Filtering
Diagnosis Filtering
Admission Month Filtering
Gender Filtering
Bed Resource Filtering

Files Created
dashboard/
├── dashboard_storyboard.pdf
└── medtrack_prototype.twbx

Milestone 2 Deliverables
generate_hospital_kpis.py
hospital_final_dataset.xlsx
hospital_kpi_summary.xlsx
dashboard_storyboard.pdf
medtrack_prototype.twbx

Project Workflow
Hospital Data Collection
        ↓
Data Cleaning & Transformation
        ↓
Feature Engineering
        ↓
Healthcare KPI Engineering
        ↓
Dashboard Storyboard
        ↓
Tableau Dashboard Development
        ↓
Interactive Dashboard Prototype

Current Project Status
Milestone 1 – Completed
Milestone 2 – Completed
Milestone 3 – In Progress

## Author

Keerthi K M

Computer Science and Engineering (AI & ML)

JSS Academy of Technical Education, Bengaluru
