import pandas as pd


def load_file(file):
    try:

        # Streamlit uploaded file object
        if hasattr(file, "name"):
            filename = file.name.lower()

        # Local file path string
        else:
            filename = file.lower()

        if filename.endswith(".csv"):
            return pd.read_csv(file)

        elif filename.endswith(".xlsx"):
            return pd.read_excel(file)

        else:
            raise ValueError("Unsupported file format")

    except Exception:
        raise