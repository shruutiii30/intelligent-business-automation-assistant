import pandas as pd

REQUIRED_COLUMNS = ["Date", "Product", "Revenue"]

def validate_schema(df: pd.DataFrame):
    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    return True