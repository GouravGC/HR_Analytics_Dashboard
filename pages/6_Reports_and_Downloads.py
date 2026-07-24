import streamlit as st
import os
from utils import load_csv, create_download_button, PATHS
from pathlib import Path

st.set_page_config(
    page_title="Reports & Downloads",
    page_icon="⬇️",
    layout="wide"
)

st.title("⬇️ Reports and Downloads")

st.markdown("""
This section allows you to download various processed datasets and summary reports generated during the HR analytics project. These files can be used for further analysis, reporting, or integration with other systems.
""")

st.subheader("Download Cleaned Data")
st.write("The fully cleaned and feature-engineered HR dataset.")
cleaned_hr_data = load_csv("cleaned_hr_data.csv")
if not cleaned_hr_data.empty:
    create_download_button(cleaned_hr_data, "cleaned_hr_data.csv", "Download Cleaned HR Data")
else:
    st.warning("Cleaned HR data not available for download.")

st.subheader("Download SQL Query Results")
st.write("Various summary tables derived from SQL queries.")

# List all CSVs in the exports folder and provide download buttons
export_files = [f for f in os.listdir(PATHS.EXPORTS) if f.endswith('.csv')]

for filename in sorted(export_files):
    if filename != "cleaned_hr_data.csv": # Already handled above
        df_to_download = load_csv(filename)
        if not df_to_download.empty:
            st.markdown(f"--- **{filename.replace('.csv', '').replace('_', ' ').title()}** ---")
            st.dataframe(df_to_download.head())
            create_download_button(df_to_download, filename, f"Download {filename}")


st.subheader("Download Comprehensive Project Artifacts")
st.write("A zip file containing all generated data exports, visualizations (HTML/PNG), and reports.")

zip_file_path = Path("HR_Workforce_Analytics_Artifacts.rar")
if os.path.exists(zip_file_path):
    with open(zip_file_path, "rb") as file:
        btn = st.download_button(
            label="Download All Artifacts (ZIP)",
            data=file,
            file_name=zip_file_path.name,
            mime="application/zip"
        )
else:
    st.warning("Project artifacts zip file not found. Please ensure the main notebook was executed to generate the zip file.")

