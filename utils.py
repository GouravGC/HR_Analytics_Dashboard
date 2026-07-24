import json
import os
from pathlib import Path
import pandas as pd
from PIL import Image
import plotly.io as pio
import streamlit as st
import streamlit.components.v1 as components


# --- Path Constants ---
class PATHS:
  ARTIFACTS = Path("artifacts")
  DATA = ARTIFACTS / "data"
  EXPORTS = DATA / "exports"
  VISUALIZATIONS = ARTIFACTS / "visualizations"
  HTML_PLOTS = VISUALIZATIONS / "html"
  IMAGE_PLOTS = VISUALIZATIONS / "images"  # Fallback for PNGs
  REPORTS = ARTIFACTS / "reports"

  # Ensure directories exist
  for path in [DATA, EXPORTS, VISUALIZATIONS, HTML_PLOTS, IMAGE_PLOTS, REPORTS]:
    path.mkdir(parents=True, exist_ok=True)


# --- Helper Functions ---


def load_csv(filename: str) -> pd.DataFrame:
  """Loads a CSV file from the exports directory."""
  try:
    return pd.read_csv(PATHS.EXPORTS / filename)
  except FileNotFoundError:
    st.error(f"Error: CSV file '{filename}' not found in {PATHS.EXPORTS}.")
    return pd.DataFrame()


def load_json(filename: str) -> dict:
  """Loads a JSON file from the exports or assets directory."""
  for path_dir in [PATHS.EXPORTS, PATHS.ARTIFACTS / "assets"]:
    try:
      with open(path_dir / filename, "r") as f:
        return json.load(f)
    except FileNotFoundError:
      continue
  st.error(
      f"Error: JSON file '{filename}' not found in {PATHS.EXPORTS} or"
      f" {PATHS.ARTIFACTS / 'assets'}."
  )
  return {}


def load_html_plot(filename, title=None):
    """
    Loads a Plotly figure from a JSON file and displays it.
    """

    json_path = PATHS.VISUALIZATIONS / "json" / f"{filename}.json"

    if title:
        st.subheader(title)

    if not json_path.exists():
        st.warning(f"Plot '{filename}.json' not found.")
        return

    try:
        fig = pio.read_json(json_path)

        fig.update_layout(
            autosize=True,
            height=700,
            margin=dict(l=20, r=20, t=50, b=20),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "responsive": True,
                "displaylogo": False,
                "scrollZoom": True,
                "modeBarButtonsToRemove": [
                    "lasso2d",
                    "select2d"
                ],
            },
        )

    except Exception as e:
        st.error(f"Error loading plot '{filename}': {e}")

def load_image(
    filename: str,
    caption: str = "",
    folder: Path = PATHS.ARTIFACTS / "assets",
    full_screen: bool = False,
):
  """Loads and displays an image file.

  Set full_screen=True on your first page to remove margins.
  """
  image_path = folder / filename
  if image_path.exists():
    if full_screen:
      # Injects CSS to remove main container padding for true edge-to-edge look
      st.markdown(
          """
                <style>
                    /* Remove Streamlit padding for full-screen hero image */
                    .block-container {
                        padding-top: 0rem !important;
                        padding-bottom: 0rem !important;
                        padding-left: 0rem !important;
                        padding-right: 0rem !important;
                        max-width: 100% !important;
                    }
                </style>
            """,
          unsafe_allow_html=True,
      )

    # Replaced deprecated use_column_width with use_container_width
    st.image(str(image_path), caption=caption, use_container_width=True)
  else:
    st.warning(f"Image '{filename}' not found in {folder}.")


def create_download_button(df: pd.DataFrame, filename: str, label: str):
  """Creates a download button for a DataFrame."""
  csv = df.to_csv(index=False).encode("utf-8")
  st.download_button(
      label=label,
      data=csv,
      file_name=filename,
      mime="text/csv",
  )


def display_kpis(kpis: dict):
  """Displays KPIs in a structured format."""
  st.subheader("Key Performance Indicators")
  cols = st.columns(len(kpis))
  for i, (kpi_name, kpi_value) in enumerate(kpis.items()):
    with cols[i]:
      st.metric(label=kpi_name, value=kpi_value)