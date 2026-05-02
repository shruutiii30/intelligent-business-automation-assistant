import streamlit as st


def render_sidebar():

    st.sidebar.title("Business Assistant")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Upload Data",
            "Dashboard",
            "AI Insights",
            "Reports"
        ]
    )

    return page