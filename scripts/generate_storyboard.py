import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_storyboard_pdf():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(project_dir, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    pdf_path = os.path.join(docs_dir, 'dashboard_storyboard.pdf')
    
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=22, leading=26, textColor=colors.HexColor('#1E3A8A'), spaceAfter=10)
    h1_style = ParagraphStyle('Heading1Custom', parent=styles['Heading2'], fontSize=15, leading=18, textColor=colors.HexColor('#1E40AF'), spaceBefore=12, spaceAfter=6)
    h2_style = ParagraphStyle('Heading2Custom', parent=styles['Heading3'], fontSize=12, leading=15, textColor=colors.HexColor('#0F766E'), spaceBefore=8, spaceAfter=4)
    body_style = ParagraphStyle('BodyCustom', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#1F2937'))
    bullet_style = ParagraphStyle('BulletCustom', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#374151'), leftIndent=12)
    
    elements = []
    
    # Title & Header
    elements.append(Paragraph("MedTrack_DV - Dashboard Storyboard & Wireframe Specification", title_style))
    elements.append(Paragraph("<b>Author:</b> Healthcare Data Analytics Team &nbsp;&nbsp;|&nbsp;&nbsp; <b>Deliverable:</b> Module 4 Prototype Specification", body_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563EB'), spaceBefore=8, spaceAfter=12))
    
    # Overview
    elements.append(Paragraph("1. Executive Summary & Workbook Architecture", h1_style))
    elements.append(Paragraph("The <b>MedTrack_DV</b> Tableau Workbook is designed as an interactive, executive-ready dashboard suite for hospital administrators, clinical operations managers, and department heads. The workbook unifies four core operational views into a single, cohesive user interface connected via global filters and parameter actions.", body_style))
    elements.append(Spacer(1, 8))
    
    arch_data = [
        ["Dashboard Name", "Core Focus & Key Performance Indicators", "Target Audience"],
        ["Hospital Overview", "Total Admissions, Occupancy Rate %, ALOS, Readmission %, Bed Utilization %, Efficiency Score", "C-Suite, Medical Directors"],
        ["Patient Flow", "Admission vs. Discharge trends, Stay Duration distribution, Peak Load tracking", "Operations Managers, Triage"],
        ["Department Analytics", "Department Volume, Efficiency Scores, Cost per Patient, Readmission by Specialty", "Department Heads, Chief of Surgery"],
        ["Resource Utilization", "Bed Utilization %, Staff Allocation Ratio, Equipment Usage (MRI, Ventilators)", "Resource Allocation, Nursing Lead"]
    ]
    t_arch = Table(arch_data, colWidths=[120, 270, 150])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F3F4F6'), colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(t_arch)
    elements.append(Spacer(1, 14))
    
    # Global Filters & Navigation Section
    elements.append(Paragraph("2. Global Interactivity, Navigation & Parameter Actions", h1_style))
    elements.append(Paragraph("<b>Global Filter Bar:</b> Displayed on top of every dashboard container for synchronized cross-filtering:", body_style))
    elements.append(Paragraph("• <b>Date Range Filter:</b> Slider & Dropdown (Default: Full Year 2024).", bullet_style))
    elements.append(Paragraph("• <b>Hospital / Region Filter:</b> Multi-select dropdown (City Care, Green Valley, Sunrise, Metro Health, HealthPlus).", bullet_style))
    elements.append(Paragraph("• <b>Department Filter:</b> Multi-select dropdown (Cardiology, Surgery, Pediatrics, ICU, Emergency, Gen Med, Orthopedics).", bullet_style))
    elements.append(Paragraph("• <b>Patient Type Filter:</b> Inpatient, Outpatient, Emergency, Day Care.", bullet_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph("<b>Navigation Actions:</b> Embedded top tab bar with active state highlights allowing seamless switching between Overview, Patient Flow, Department Analytics, and Resource Utilization.", body_style))
    
    elements.append(PageBreak())
    
    # Dashboard 1: Hospital Overview
    elements.append(Paragraph("3. Dashboard 1 Wireframe: Hospital Overview", h1_style))
    elements.append(Paragraph("<b>Layout Grid (1920 x 1080 Desktop Standard):</b>", h2_style))
    
    ov_wireframe = [
        ["Top KPI Bar (6 Cards)", "Total Admissions (5,015) | Occupancy Rate (82.1%) | ALOS (5.1 Days) | Readmission Rate (13.0%) | Bed Utilization (82.1%) | Efficiency (73.0)"],
        ["Main Chart 1 (Left 60%)", "Monthly Admission & Discharge Trends (Dual Line Chart with YoY Comparison)"],
        ["Main Chart 2 (Right 40%)", "Occupancy & Bed Utilization Trend (Area Chart with Threshold Indicator @ 85%)"],
        ["Bottom Left (50%)", "Readmission Rate by Specialty & Severity (Bar Chart)"],
        ["Bottom Right (50%)", "Regional Hospital Performance Comparison (Geographic Map / Ranked Horizontal Bars)"]
    ]
    t_ov = Table(ov_wireframe, colWidths=[150, 390])
    t_ov.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#0F766E')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t_ov)
    elements.append(Spacer(1, 14))
    
    # Dashboard 2: Patient Flow
    elements.append(Paragraph("4. Dashboard 2 Wireframe: Patient Flow Analytics", h1_style))
    elements.append(Paragraph("<b>Layout Grid & Visualizations:</b>", h2_style))
    
    pf_wireframe = [
        ["Top Summary", "Patient Volume Flow Indicator | Average Stay Metric Cards | Peak Load Alert Banner"],
        ["Upper Container", "Monthly Admissions vs. Discharges Flow (Stacked Area Chart showing Net Inflow/Outflow)"],
        ["Middle Container", "Length of Stay (LOS) Distribution by Severity & Department (Box Plot / Histogram)"],
        ["Lower Container", "Peak Patient Admission Load Heatmap (Days of Week vs. Hours/Months)"]
    ]
    t_pf = Table(pf_wireframe, colWidths=[150, 390])
    t_pf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#1E40AF')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t_pf)
    elements.append(Spacer(1, 14))
    
    # Dashboard 3: Department Analytics
    elements.append(Paragraph("5. Dashboard 3 Wireframe: Department Analytics", h1_style))
    dept_wireframe = [
        ["Top Parameter Selector", "Select Primary Department vs. Benchmark Department (Dynamic Parameter Action)"],
        ["Left Matrix", "Department Efficiency Score vs. Patient Satisfaction Scatter Plot"],
        ["Right Breakdown", "Treatment Cost per Patient & Avg Length of Stay Bar Charts"],
        ["Bottom Matrix", "Readmission Rate & Severity Breakdown Grid per Specialty"]
    ]
    t_dept = Table(dept_wireframe, colWidths=[150, 390])
    t_dept.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#374151')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t_dept)
    elements.append(Spacer(1, 14))
    
    # Dashboard 4: Resource Utilization
    elements.append(Paragraph("6. Dashboard 4 Wireframe: Resource Utilization", h1_style))
    res_wireframe = [
        ["Top KPI Gauge", "Bed Utilization Rate Gauge (82.1%) | Staff Ratio Gauge | Critical Equipment Active %"],
        ["Upper View", "Bed Capacity & Occupancy Heatmap by Hospital Wing / Department"],
        ["Lower Left", "Staff Allocation Monitoring (Doctor/Nurse-to-Patient Ratio Bar Chart)"],
        ["Lower Right", "High-Value Equipment Usage (Ventilator, MRI, CT Scanner Distribution Donut Chart)"]
    ]
    t_res = Table(res_wireframe, colWidths=[150, 390])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#9D174D')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(t_res)
    
    doc.build(elements)
    print(f"Generated PDF storyboard specification at: {pdf_path}")

if __name__ == '__main__':
    create_storyboard_pdf()
