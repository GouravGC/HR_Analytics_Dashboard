import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Power BI Dashboard",
    page_icon="📊",
    layout="wide"
)


# Paths
POWERBI_FOLDER = Path("powerbi")

PREVIEW_IMAGE = POWERBI_FOLDER / "HR_Workforce_Dashboard.png"

PBIX_FILE_1 = POWERBI_FOLDER / "HR_Workforce_Analytics.pbix"
PBIX_FILE_2 = POWERBI_FOLDER / "hr_analytics.pbix"


# Title
st.title("📊 HR Workforce Analytics - Power BI Dashboard")


st.markdown(
    """
    This page showcases the Power BI dashboards created for the 
    HR Workforce Analytics project.

    The reports provide interactive insights into:

    - Employee demographics
    - Attrition analysis
    - Department-level workforce trends
    - Salary analysis
    - Job satisfaction metrics
    - Workforce performance indicators
    """
)


st.divider()


# Preview Image

st.subheader("🖼️ Power BI Dashboard Preview")


if PREVIEW_IMAGE.exists():

    st.image(
        PREVIEW_IMAGE,
        caption="HR Workforce Analytics Dashboard Preview",
        use_container_width=True
    )

else:
    st.warning(
        "Dashboard preview image not found. "
        "Please add HR_Workforce_Dashboard.png inside the PowerBI folder."
    )


st.divider()


# Download Section

st.subheader("📥 Download Power BI Reports")


# First PBIX

if PBIX_FILE_1.exists():

    with open(PBIX_FILE_1, "rb") as file:

        st.download_button(
            label="⬇️ Download HR Workforce Analytics PBIX",
            data=file,
            file_name=PBIX_FILE_1.name,
            mime="application/octet-stream"
        )

else:
    st.warning("HR_Workforce_Analytics.pbix file not found.")



# Second PBIX

if PBIX_FILE_2.exists():

    with open(PBIX_FILE_2, "rb") as file:

        st.download_button(
            label="⬇️ Download HR Analytics PBIX",
            data=file,
            file_name=PBIX_FILE_2.name,
            mime="application/octet-stream"
        )

else:
    st.warning("hr_analytics.pbix file not found.")


st.divider()


st.info(
    """
    📌 To explore these dashboards:
    
    1. Download the PBIX file.
    2. Open it using Microsoft Power BI Desktop.
    3. Interact with filters, visuals, and reports.

    Microsoft Power BI Desktop is required to open PBIX files.
    """
)