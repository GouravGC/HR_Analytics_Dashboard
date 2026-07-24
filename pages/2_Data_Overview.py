import streamlit as st
import pandas as pd
from utils import load_csv

st.set_page_config(
    page_title="Data Overview",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Data Overview")

st.markdown("""
This section provides a detailed look at the cleaned HR dataset. You can explore the raw data, its structure, and key descriptive statistics after the data cleaning and feature engineering processes.
""")

cleaned_df = load_csv("cleaned_hr_data.csv")

if not cleaned_df.empty:

    st.subheader("Cleaned HR Data")
    st.dataframe(cleaned_df, use_container_width=True)

    st.subheader("DataFrame Information")

    st.write(f"**Shape:** {cleaned_df.shape[0]} rows × {cleaned_df.shape[1]} columns")

    info_df = pd.DataFrame({
        "Column": cleaned_df.columns,
        "Data Type": cleaned_df.dtypes.astype(str),
        "Non-Null Count": cleaned_df.count().values,
        "Missing Values": cleaned_df.isnull().sum().values,
        "Unique Values": cleaned_df.nunique().values
    })

    st.dataframe(info_df, use_container_width=True)

    st.subheader("Descriptive Statistics")

    st.markdown("#### Numerical Columns")
    st.dataframe(
        cleaned_df.describe(),
        use_container_width=True
    )

    st.markdown("#### Categorical Columns")
    st.dataframe(
        cleaned_df.describe(include="object"),
        use_container_width=True
    )

else:
    st.error(
        "Cleaned HR data not available. Please ensure the main notebook was executed to generate artifacts."
    )