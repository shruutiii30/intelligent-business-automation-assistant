from src.ingestion.loader import load_file
from src.ingestion.validator import validate_schema
from src.cleaning.preprocessor import clean_data
from src.analysis.kpi_engine import generate_kpis
from src.visualization.charts import plot_revenue_trend


def main():

    file_path = "data/raw/sales_sample.csv"

    # Step 1: Load data
    df = load_file(file_path)

    # Step 2: Validate schema
    validate_schema(df)

    # Step 3: Clean data
    df = clean_data(df)

    # Step 4: Generate KPIs
    kpis = generate_kpis(df)

    # Step 5: Print results
    print("\nCLEANED DATA:")
    print(df)

    print("\nBUSINESS KPIs:")
    print(kpis)

    plot_revenue_trend(df)

if __name__ == "__main__":
    main()