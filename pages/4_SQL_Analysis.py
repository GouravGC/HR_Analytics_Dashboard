import streamlit as st
from utils import load_csv

st.set_page_config(
    page_title="SQL Analysis",
    page_icon="💾",
    layout="wide"
)

st.title("💾 SQL Analysis Results")

st.markdown("""
This section displays the outputs of various SQL queries executed during the analysis phase. These tables provide direct data-driven answers to specific HR questions.
""")

# --- Load specific SQL query results (CSVs) ---
st.subheader("Department-wise Attrition Rates")
df_dept_attrition = load_csv("department_attrition.csv")
if not df_dept_attrition.empty: st.dataframe(df_dept_attrition)

st.subheader("Gender Distribution")
df_gender = load_csv("gender_distribution.csv")
if not df_gender.empty: st.dataframe(df_gender)

st.subheader("Age Group Distribution")
df_age_group = load_csv("agegroup_distribution.csv")
if not df_age_group.empty: st.dataframe(df_age_group)

st.subheader("Marital Status Distribution")
df_marital = load_csv("marital_status.csv")
if not df_marital.empty: st.dataframe(df_marital)

st.subheader("Education Level Distribution")
df_education_level = load_csv("education_level.csv")
if not df_education_level.empty: st.dataframe(df_education_level)

st.subheader("Education Field Distribution")
df_education_field = load_csv("education_field.csv")
if not df_education_field.empty: st.dataframe(df_education_field)

st.subheader("Average Salary by Department")
df_salary_dept = load_csv("Salary_by_Department.csv")
if not df_salary_dept.empty: st.dataframe(df_salary_dept)

st.subheader("Average Salary by Job Role")
df_salary_jobrole = load_csv("Salary_by_Job_Role.csv")
if not df_salary_jobrole.empty: st.dataframe(df_salary_jobrole)

st.subheader("Promotion Status Distribution")
df_promotion_status = load_csv("promotion_status_distribution.csv")
if not df_promotion_status.empty: st.dataframe(df_promotion_status)

st.subheader("Experience Level Distribution")
df_experience_level = load_csv("experience_level_distribution.csv")
if not df_experience_level.empty: st.dataframe(df_experience_level)

st.subheader("Job Role Attrition")
df_job_attrition = load_csv("Job_Role_Attrition.csv")
if not df_job_attrition.empty: st.dataframe(df_job_attrition)

st.subheader("Overtime vs. Attrition")
df_overtime_attrition = load_csv("Overtime_vs_Attrition.csv")
if not df_overtime_attrition.empty: st.dataframe(df_overtime_attrition)

st.subheader("Job Satisfaction Attrition")
df_job_satisfaction_attrition = load_csv("Job_Satisfaction_Attrition.csv")
if not df_job_satisfaction_attrition.empty: st.dataframe(df_job_satisfaction_attrition)


# Add more SQL result displays as needed from your `artifacts/data/exports`
