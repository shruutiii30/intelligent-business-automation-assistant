import pandas as pd


def clean_data(df: pd.DataFrame):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df["Revenue"] = df["Revenue"].fillna(0)
    df["Product"] = df["Product"].fillna("Unknown")

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    return df