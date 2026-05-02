import streamlit as st
import plotly.express as px


def show_revenue_chart(df):

    daily_sales = (
        df.groupby("Date")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Revenue",
        title="Revenue Trend"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )