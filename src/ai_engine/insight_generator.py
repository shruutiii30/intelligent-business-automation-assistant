import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_insights(kpis):

    prompt = f"""
    Analyze these business KPIs and provide:

    1. Business performance summary
    2. Risks
    3. Recommendations

    KPI Data:
    {kpis}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text