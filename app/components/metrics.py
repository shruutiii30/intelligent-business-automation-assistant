import streamlit as st


def show_metrics(kpis):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Revenue",
        f"₹{kpis['total_revenue']}"
    )

    col2.metric(
        "Orders",
        kpis['total_orders']
    )

    col3.metric(
        "Top Product",
        kpis['top_product']
    )

    col4.metric(
        "Avg Order",
        f"₹{round(kpis['avg_order_value'],2)}"
    )
    