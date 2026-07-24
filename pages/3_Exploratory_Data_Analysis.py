import streamlit as st
from utils import load_html_plot

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Exploratory Data Analysis")

st.markdown("""
This section presents various interactive visualizations to understand the distributions, relationships, and patterns within the HR data. Dive into demographics, compensation, satisfaction, and more.
""")

st.subheader("Employee Demographics")
col1, col2 = st.columns(2)
with col1:
    load_html_plot("gender_distribution", "Gender Distribution")
with col2:
    load_html_plot("agegroup_distribution", "Age Group Distribution")

col3, col4 = st.columns(2)
with col3:
    load_html_plot("marital_status", "Marital Status Distribution")
with col4:
    load_html_plot("education_level", "Education Level Distribution")

load_html_plot("education_field", "Education Field Distribution")

st.subheader("Compensation Analysis")
load_html_plot("salary_department", "Average Salary by Department")
load_html_plot("salary_jobrole", "Salary by Job Role")

col5, col6 = st.columns(2)
with col5:
    load_html_plot("salary_gender", "Average Salary by Gender")
with col6:
    load_html_plot("salary_slab", "Salary Slab Distribution")

st.subheader("Career & Satisfaction Metrics")
col7, col8 = st.columns(2)
with col7:
    load_html_plot("promotion_status", "Promotion Status Distribution")
with col8:
    load_html_plot("experience_level", "Experience Level Distribution")

load_html_plot("department_tenure", "Average Tenure by Department")

load_html_plot("department_performance", "Department Performance Rating")

col9, col10 = st.columns(2)
with col9:
    load_html_plot("department_worklife", "Department Work-Life Balance")
with col10:
    load_html_plot("department_distance", "Average Distance From Home by Department")

