import pandas as pd


def validate_schema(
    df: pd.DataFrame
):

    if df.empty:

        raise ValueError(
            "Uploaded file is empty."
        )

    if len(df.columns) < 2:

        raise ValueError(
            "Dataset must contain at least 2 columns."
        )

    return True