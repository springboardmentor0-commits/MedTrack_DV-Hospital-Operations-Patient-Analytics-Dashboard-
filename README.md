# MedTrack_DV - Hospital Operations & Patient Analytics Dashboard

## Project Overview
**MedTrack_DV** is a comprehensive hospital operations and patient analytics project designed to transform healthcare operational data into actionable insights through interactive Tableau dashboards and data pipelines.

---

## Repository Structure
```
MedTrack_DV/
├── data/
│   ├── hospital_raw_data.csv     # Raw dataset generated from hospital operations & admissions
│   └── hospital_cleaned.csv     # Cleaned, standardized, Tableau-ready dataset
├── scripts/
│   ├── data_collection.py        # Python script to generate & integrate healthcare datasets
│   ├── build_notebook.py         # Utility script to build hospital_cleaning.ipynb
│   └── run_cleaning.py           # Script to execute data cleaning pipeline
├── hospital_cleaning.ipynb       # Module 2 Deliverable: Jupyter Notebook for data cleaning
├── dashboard/                    # Tableau workbook files (.twbx)
├── docs/                         # Documentation & QA reports
├── .gitignore
└── README.md
```

---

## Milestone 1 Status: Data Collection and Preparation (Completed)

### Module 1: Hospital Data Collection
- **Deliverables**:
  - `data/hospital_raw_data.csv` (and `hospital_raw_data.csv`)
  - `scripts/data_collection.py`
- **Evaluation Criteria**:
  - Dataset integration: **Passed** (5,075 raw records generated)
  - Dataset completeness: **99.49%** (Target > 95%)

### Module 2: Data Cleaning & Transformation
- **Deliverables**:
  - `data/hospital_cleaned.csv` (and `hospital_cleaned.csv`)
  - `hospital_cleaning.ipynb`
- **Evaluation Criteria**:
  - Duplicate records removed: **60 duplicates removed** (5,015 clean records)
  - Missing values rate: **0.00%** (Target < 2%)
  - Department names standardized across 7 core medical departments.
  - Healthcare metrics normalized (Length of Stay, Daily Treatment Cost, Department Efficiency Score).

---

## Milestone 2 Status: KPI Engineering and Dashboard Planning (Completed)

### Module 3: Hospital KPI Engineering
- **Deliverables**:
  - `data/hospital_final_dataset.xlsx` (and `hospital_final_dataset.xlsx`)
  - `scripts/generate_hospital_kpis.py`
- **Evaluation Criteria**:
  - All KPIs calculated: Total Admissions (5,015), Occupancy Rate (82.06%), ALOS (5.12 Days), 30-Day Readmission Rate (13.02%), Bed Utilization Rate (82.06%), Department Efficiency Score (72.99).
  - Dataset optimized for Tableau Desktop/Public with multiple structured sheets.

### Module 4: Dashboard Planning & Prototyping
- **Deliverables**:
  - `docs/dashboard_storyboard.pdf`
  - `dashboard/medtrack_prototype.twbx` (and `medtrack_prototype.twbx`)
- **Evaluation Criteria**:
  - Wireframes and interactive storyboard layout specs approved.
  - Packaged Tableau prototype workbook (.twbx) initialized.

---

## How to Run in VS Code

1. **Open Workspace in VS Code**:
   Open `C:\Users\manda\Documents\Infosys Hospital Analysis\MedTrack_DV` in VS Code.

2. **Run Data Collection**:
   ```powershell
   python scripts/data_collection.py
   ```

3. **Execute Data Cleaning Notebook**:
   ```powershell
   python scripts/run_cleaning.py
   ```

4. **Generate Hospital KPIs & Excel Workbook**:
   ```powershell
   python scripts/generate_hospital_kpis.py
   ```

5. **Generate Storyboard & Prototype Deliverables**:
   ```powershell
   python scripts/generate_storyboard.py
   python scripts/build_tableau_prototype.py
   ```

---

## License & Contribution
Developed for Hospital Operations & Healthcare Analytics Dashboard suite.
