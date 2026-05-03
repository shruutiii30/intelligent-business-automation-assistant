import streamlit as st


def show_metrics(kpis):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Value",
        round(kpis["total_value"], 2)
    )

    col2.metric(
        "Average",
        round(kpis["avg_value"], 2)
    )

    col3.metric(
        "Records",
        kpis["total_records"]
    )

    col4.metric(
        "Top Category",
        kpis["top_category"]
    )