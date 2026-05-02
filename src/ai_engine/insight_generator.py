import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_ai_insights(kpis):

    prompt = f"""
    Analyze these business KPIs and give executive insights:

    {kpis}

    Include:
    1. Business performance
    2. Risks
    3. Recommendations
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content