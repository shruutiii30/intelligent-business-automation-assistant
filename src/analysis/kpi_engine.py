import pandas as pd


def generate_kpis(
    df: pd.DataFrame,
    schema: dict
):

    numeric_columns = schema[
        "numeric_columns"
    ]

    categorical_columns = schema[
        "categorical_columns"
    ]

    if not numeric_columns:
        raise ValueError(
            "No numeric columns found."
        )

    main_metric = numeric_columns[0]

    total_value = df[
        main_metric
    ].sum()

    avg_value = df[
        main_metric
    ].mean()

    total_records = len(df)

    top_category = "N/A"

    if categorical_columns:

        category_col = categorical_columns[0]

        top_category = (
            df.groupby(category_col)[main_metric]
            .sum()
            .idxmax()
        )

    return {
        "main_metric": main_metric,
        "total_value": total_value,
        "avg_value": avg_value,
        "total_records": total_records,
        "top_category": top_category
    }