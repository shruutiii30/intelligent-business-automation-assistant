from src.ingestion.loader import load_file
from src.ingestion.validator import validate_schema
from src.cleaning.preprocessor import clean_data


def main():
    file_path = "data/raw/sales_sample.csv"

    # Step 1: Load file
    df = load_file(file_path)

    # Step 2: Validate schema
    validate_schema(df)

    # Step 3: Clean data
    df = clean_data(df)

    # Step 4: Print cleaned data
    print(df)


if __name__ == "__main__":
    main()