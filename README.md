app_url = https://hranalyticsdashboard-gc.streamlit.app/

# 🏢 HR Workforce Intelligence & Analytics Dashboard

This project delivers an end-to-end HR Analytics solution, transforming raw employee data into actionable business intelligence through a Streamlit interactive dashboard. It leverages SQL for data querying, Python for cleaning and analysis, and Plotly for rich visualizations.

## 🚀 Project Overview

The objective is to provide HR teams with comprehensive analytics to understand workforce trends, employee demographics, compensation, promotions, diversity, and attrition. The dashboard aims to answer critical business questions and support data-driven decision-making.

## ✨ Features

- **Interactive Dashboard:** Dynamic views of key HR metrics and trends.
- **Employee Demographics:** Visualizations of age, gender, marital status, and education distribution.
- **Compensation Analysis:** Insights into salary distribution by department, job role, and gender.
- **Attrition Deep Dive:** Identification of departments, job roles, and factors contributing to attrition.
- **Career Progression:** Analysis of promotion status and tenure within the company.
- **Data Overview:** Detailed exploration of the cleaned dataset.
- **Downloadable Reports:** Access to processed data and summary reports.

## 📊 Dataset

The project utilizes an HR Analytics dataset containing various employee attributes such as `EmpID`, `Age`, `Department`, `MonthlyIncome`, `Attrition`, `YearsAtCompany`, `JobRole`, and more. The dataset undergoes a thorough cleaning and feature engineering process to ensure data quality and enrich analytical capabilities.

## 📂 Folder Structure

```
HR_Analytics_Dashboard/
├── app.py                      # Main Streamlit application
├── utils.py                    # Helper functions and path constants
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Files/folders to ignore in Git
├── pages/                      # Streamlit multi-page application
│   ├── 1_Dashboard.py
│   ├── 2_Data_Overview.py
│   ├── 3_Exploratory_Data_Analysis.py
│   ├── 4_SQL_Analysis.py
│   ├── 5_Business_Insights.py
│   └── 6_Reports_and_Downloads.py
└── artifacts/                  # Generated data, visualizations, and reports
    ├── data/
    │   ├── raw/
    │   ├── cleaned/
    │   └── exports/            # Cleaned data, SQL query results (CSVs)
    ├── visualizations/
    │   ├── html/               # Interactive Plotly charts (HTML)
    │   └── images/             # Static chart images (PNG fallback)
    ├── reports/
    ├── assets/
    └── dashboard/
```

## 🛠️ Technologies

- Python (Pandas, NumPy, Plotly, Streamlit)
- SQL (SQLite)
- Power BI (for external executive dashboard, if available)

## ⚙️ Installation

1.  **Clone the repository (or download the project files):**
    ```bash
    git clone <repository_url>
    cd HR_Analytics_Dashboard
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure `artifacts/` folder is populated:**
    Run the provided Jupyter/Colab notebook (`HR_Analytics_Project.ipynb`) from top to bottom to generate all `artifacts/` (cleaned data, SQL exports, Plotly HTML files, etc.). This Streamlit app relies on these pre-generated files.

## 🚀 Usage

To run the Streamlit application:

```bash
streamlit run app.py
```

This will open the application in your default web browser.

## 🌐 Deployment

This application can be deployed on various platforms that support Streamlit applications, such as Streamlit Community Cloud, Heroku, or Google Cloud Run. Ensure that all artifacts are correctly accessible in the deployment environment.

## 📸 Screenshots (Placeholders)

*(Add screenshots of your Streamlit dashboard pages here)*

### Homepage
![Homepage Screenshot]("dashboard_preview/dashboard_preview.png")

### Dashboard Overview
![Dashboard Screenshot](https://via.placeholder.com/800x450?text=Dashboard+Page+Screenshot)

### EDA Visualizations
![EDA Screenshot](https://via.placeholder.com/800x450?text=EDA+Page+Screenshot)

## 📈 Power BI Dashboard (If Available)

An executive Power BI dashboard complements this project, offering interactive data exploration and drill-down capabilities not fully replicated in Streamlit. 

*(Link to Power BI Report or embed a screenshot if publicly accessible)*

![Power BI Dashboard Placeholder]("powerbi/HR_Workforce_Dashboard.png")
