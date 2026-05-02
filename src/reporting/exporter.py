import pandas as pd


def export_report(df: pd.DataFrame):

    output_path = "data/processed/final_report.csv"

    df.to_csv(
        output_path,
        index=False
    )

    return output_path