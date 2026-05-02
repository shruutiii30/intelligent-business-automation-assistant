import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from src.ingestion.loader import load_file
from src.ingestion.validator import validate_schema
from src.cleaning.preprocessor import clean_data
from src.analysis.kpi_engine import generate_kpis
from src.ai_engine.insight_generator import generate_ai_insights


st.title("Intelligent Business Automation Assistant")


uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx"]
)


if uploaded_file:

    # Load
    df = load_file(uploaded_file)

    # Validate
    validate_schema(df)

    # Clean
    df = clean_data(df)

    # KPIs
    kpis = generate_kpis(df)

    st.subheader("Business KPIs")
    st.write(kpis)

    # AI Insights
    insights = generate_ai_insights(kpis)

    st.subheader("AI Business Insights")
    st.write(insights)

    # Data Preview
    st.subheader("Processed Data")
    st.dataframe(df)