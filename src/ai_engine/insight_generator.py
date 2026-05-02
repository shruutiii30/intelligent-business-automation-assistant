def generate_ai_insights(kpis):

    total_revenue = kpis["total_revenue"]
    top_product = kpis["top_product"]
    avg_order_value = kpis["avg_order_value"]

    return f"""
    BUSINESS PERFORMANCE SUMMARY

    Total Revenue Generated: ₹{total_revenue}

    Top Performing Product: {top_product}

    Average Order Value: ₹{avg_order_value:.2f}

    KEY INSIGHTS:

    1. Revenue generation is stable based on current transactions.

    2. {top_product} is driving the highest business value.

    3. Consider increasing inventory allocation for high-performing products.

    4. Monitor underperforming product categories for optimization.

    5. Track revenue trends continuously for growth forecasting.
    """