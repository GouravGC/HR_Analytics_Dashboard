import streamlit as st
from utils import load_csv, load_html_plot, display_kpis

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Key HR Dashboard")

# --- Load Data ---
executive_summary = load_csv("executive_summary.csv")
department_attrition_df = load_csv("department_attrition.csv")
job_role_attrition_df = load_csv("Job_Role_Attrition.csv")

# --- Display KPIs ---
if not executive_summary.empty:
    kpis = {
        "Total Employees": executive_summary['TotalEmployees'].iloc[0],
        "Attrition Count": executive_summary['AttritionCount'].iloc[0],
        "Attrition Rate": f"{executive_summary['AttritionRate'].iloc[0]}%",
        "Average Salary": f"${executive_summary['AverageSalary'].iloc[0]:,.2f}",
        "Average Age": f"{executive_summary['AverageAge'].iloc[0]:.1f} years"
    }
    display_kpis(kpis)

st.markdown("--- ")

if not department_attrition_df.empty:
    load_html_plot("department_attrition", "Department-wise Attrition Rate")
else:
    st.warning("Department attrition data not available.")

if not job_role_attrition_df.empty:
    load_html_plot("jobrole_attrition", "Attrition Count by Job Role")
else:
    st.warning("Job role attrition data not available.")

st.markdown("""
This dashboard provides an executive summary of key HR metrics and highlights critical areas like departmental and job role attrition. These insights are crucial for strategic HR planning and intervention.
""")
