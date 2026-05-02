import matplotlib.pyplot as plt


def plot_revenue_trend(df):

    daily_sales = (
        df.groupby("Date")["Revenue"]
        .sum()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(daily_sales.index, daily_sales.values)

    plt.title("Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()