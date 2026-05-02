from src.ingestion.loader import load_file
from src.ingestion.validator import validate_schema
from src.cleaning.preprocessor import clean_data
from src.analysis.kpi_engine import generate_kpis
from src.visualization.charts import plot_revenue_trend
from src.ai_engine.insight_generator import generate_ai_insights


def main():

    file_path = "data/raw/sales_sample.csv"

    # Load
    df = load_file(file_path)

    # Validate
    validate_schema(df)

    # Clean
    df = clean_data(df)

    # Generate KPIs
    kpis = generate_kpis(df)

    print("\nKPIs:\n")
    print(kpis)

    # Visualization
    plot_revenue_trend(df)

    # AI Insights
    insights = generate_ai_insights(kpis)

    print("\nAI INSIGHTS:\n")
    print(insights)


if __name__ == "__main__":
    main()