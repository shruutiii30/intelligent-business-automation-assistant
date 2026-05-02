import pandas as pd


def generate_kpis(df: pd.DataFrame):

    total_revenue = df["Revenue"].sum()

    total_orders = len(df)

    top_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .idxmax()
    )

    avg_order_value = total_revenue / total_orders

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "top_product": top_product,
        "avg_order_value": avg_order_value
    }