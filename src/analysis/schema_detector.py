import pandas as pd


def detect_schema(df: pd.DataFrame):

    date_columns = []
    numeric_columns = []
    categorical_columns = []

    for column in df.columns:

        if pd.api.types.is_datetime64_any_dtype(
            df[column]
        ):
            date_columns.append(column)

        elif pd.api.types.is_numeric_dtype(
            df[column]
        ):
            numeric_columns.append(column)

        else:
            categorical_columns.append(column)

    return {
        "date_columns": date_columns,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns
    }