def generate_ai_insights(kpis):

    metric_name = kpis["main_metric"]
    total_value = kpis["total_value"]
    avg_value = kpis["avg_value"]
    top_category = kpis["top_category"]

    return f"""
    BUSINESS PERFORMANCE SUMMARY

    Primary Metric: {metric_name}

    Total Value: {round(total_value, 2)}

    Average Value: {round(avg_value, 2)}

    Top Category: {top_category}

    KEY INSIGHTS:

    1. The dataset shows strong activity in {top_category}.

    2. Total {metric_name} generated is {round(total_value, 2)}.

    3. Average {metric_name} per record is {round(avg_value, 2)}.

    4. Focus on high-performing categories to maximize growth.

    5. Monitor low-performing segments for optimization.
    """