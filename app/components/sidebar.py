import streamlit as st


def render_sidebar():

    st.sidebar.markdown("## 📊 Business Assistant")

    page = st.sidebar.radio(
        "Navigation",
        [
            "📂 Upload Data",
            "📈 Dashboard",
            "🤖 AI Insights",
            "📄 Reports"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "AI-powered business analytics platform"
    )

    return page