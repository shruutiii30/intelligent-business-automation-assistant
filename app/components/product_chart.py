import streamlit as st
import plotly.express as px


def show_product_comparison(df):

    product_sales = (
        df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        product_sales,
        x="Product",
        y="Revenue",
        title="Product Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
