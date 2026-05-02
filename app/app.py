import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st

from components.sidebar import render_sidebar
from components.metrics import show_metrics
from components.charts import show_revenue_chart
from components.insights import show_ai_insights

from src.ingestion.loader import load_file
from src.ingestion.validator import validate_schema
from src.cleaning.preprocessor import clean_data
from src.analysis.kpi_engine import generate_kpis
from src.ai_engine.insight_generator import generate_ai_insights
from src.reporting.exporter import export_report


# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
    page_title="Intelligent Business Automation Assistant",
    page_icon="📊",
    layout="wide"
)


# ------------------------------
# CUSTOM CSS
# ------------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

h1 {
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------
# HEADER
# ------------------------------
st.title("📊 Intelligent Business Automation Assistant")
st.caption("AI-powered business analytics and reporting system")


# ------------------------------
# SIDEBAR
# ------------------------------
page = render_sidebar()


# ------------------------------
# FILE UPLOAD
# ------------------------------
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)


if uploaded_file:

    try:

        st.success("File uploaded successfully!")

        with st.spinner("Processing business data..."):

            # Load
            df = load_file(uploaded_file)

            # Validate
            validate_schema(df)

            # Clean
            df = clean_data(df)

            # KPIs
            kpis = generate_kpis(df)

            # AI Insights
            insights = generate_ai_insights(kpis)

            # Export Report
            report_path = export_report(df)

        # ============================
        # DASHBOARD SECTION
        # ============================
        st.markdown("---")
        st.subheader("📈 Business Dashboard")

        show_metrics(kpis)

        st.markdown("### Revenue Trend")
        show_revenue_chart(df)

        # ============================
        # DATA PREVIEW
        # ============================
        st.markdown("---")
        st.subheader("📄 Processed Data Preview")

        st.dataframe(
            df,
            use_container_width=True
        )

        # ============================
        # AI INSIGHTS
        # ============================
        st.markdown("---")
        show_ai_insights(insights)

        # ============================
        # DOWNLOAD SECTION
        # ============================
        st.markdown("---")
        st.subheader("⬇ Export Reports")

        with open(report_path, "rb") as file:

            st.download_button(
                label="Download Business Report",
                data=file,
                file_name="business_report.csv",
                mime="text/csv"
            )

    except Exception as e:

        st.error(
            f"Error while processing file: {str(e)}"
        )

else:

    st.info(
        "Upload a business dataset to begin analysis."
    )