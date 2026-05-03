import streamlit as st
import plotly.express as px


def show_dynamic_chart(df, schema):

    numeric_columns = schema["numeric_columns"]
    categorical_columns = schema["categorical_columns"]
    date_columns = schema["date_columns"]

    if not numeric_columns:

        st.warning(
            "No numeric columns found."
        )

        return

    metric = numeric_columns[0]

    # If date exists → trend chart
    if date_columns:

        date_col = date_columns[0]

        chart_data = (
            df.groupby(date_col)[metric]
            .sum()
            .reset_index()
        )

        fig = px.line(
            chart_data,
            x=date_col,
            y=metric,
            title=f"{metric} Trend"
        )

    # If category exists → comparison chart
    elif categorical_columns:

        category_col = categorical_columns[0]

        chart_data = (
            df.groupby(category_col)[metric]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            chart_data,
            x=category_col,
            y=metric,
            title=f"{metric} by {category_col}"
        )

    # Only numeric data
    else:

        fig = px.histogram(
            df,
            x=metric,
            title=f"{metric} Distribution"
        )

    st.plotly_chart(
        fig,
        use_container_width=True
    )