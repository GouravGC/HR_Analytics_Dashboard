import streamlit as st
import os
from utils import load_image, load_html_plot, create_download_button, PATHS

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .reportview-container {
        background: #F5F5F5;
    }
    .sidebar .sidebar-content {
        background: #FFFFFF;
    }
    header {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .plotly-container {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏢 HR Workforce Intelligence & Analytics")

st.markdown("""
Welcome to the HR Workforce Intelligence & Analytics Dashboard! This application provides comprehensive insights into various aspects of human resources data, from employee demographics and attrition to compensation and performance.
""")

st.subheader("Project Overview")
st.write("""
This project transforms raw HR data into actionable business insights using SQL, Python, Power BI, and Streamlit. It addresses key business questions related to workforce trends, employee demographics, compensation, promotions, diversity, and employee attrition.
""")

st.subheader("Features")
st.markdown("""
- **Dashboard:** Key Performance Indicators (KPIs) and high-level summaries.
- **Data Overview:** Detailed view of the cleaned dataset and its structure.
- **Exploratory Data Analysis (EDA):** Interactive visualizations covering demographics, compensation, job satisfaction, and more.
- **SQL Analysis:** Displays the results of various SQL queries used to extract specific insights.
- **Business Insights:** Summarized key findings and recommendations.
- **Reports and Downloads:** Options to download processed datasets and reports.
""")

st.subheader("Dashboard Preview")
st.image("dashboard_preview/dashboard_preview.PNG", caption="Dashboard Preview")

st.subheader("Dataset Information")
st.markdown("""
The dataset used in this project contains various attributes of employees, including personal details, job-related information, and performance metrics. It's crucial for understanding employee behavior and organizational health.
""")

st.subheader("Technology Stack")
st.markdown("""
- **Data Processing & Analysis:** Python (Pandas, NumPy)
- **Database:** SQLite (for SQL analysis)
- **Visualization:** Plotly (Interactive Charts), Matplotlib, Seaborn
- **Reporting:** Power BI (External Dashboard - *if available*)
- **Web Application:** Streamlit
""")

st.subheader("Navigation Instructions")
st.markdown("""
Use the sidebar to navigate through different sections of the application:
- **Dashboard:** Get a quick overview of key HR metrics.
- **Data Overview:** Explore the cleaned dataset.
- **Exploratory Data Analysis:** Dive deep into various interactive charts.
- **SQL Analysis:** Review results from direct database queries.
- **Business Insights:** Understand the strategic implications of the data.
- **Reports and Downloads:** Access and download compiled reports and data.
""")

st.info("This Streamlit application loads pre-generated artifacts and does not rerun the analysis. All charts are interactive JSON, with a fallback to PNG or HTML if JSON is unavailable.")
