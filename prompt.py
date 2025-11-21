import os
import openai
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import sqlite3

load_dotenv()

model = "openai/gpt-oss-120b"

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("OPENAI_API_KEY")
    
)
DB_PATH = "data.sqlite"
conn = sqlite3.connect(DB_PATH)
train = pd.read_sql("SELECT * FROM train", conn)
conn.close()

prompt = f"""
Analiza la base de datos de morosidad crediticia con las siguientes variables:
{', '.join(train.columns)}.

1. Resume la distribución de morosos vs no morosos.
2. Identifica las variables que parecen más influyentes.
3. Sugiere tres tipos de visualizaciones útiles para Power BI.
4. Propón un resumen ejecutivo de los hallazgos.
"""

response = client.responses.create(
    model=model,
    input=prompt
)

insight = response.output_text

os.makedirs("PowerBI", exist_ok=True)
with open("PowerBI/insight_openai.txt", "w", encoding="utf-8") as f:
    f.write(insight)

print("Análisis automático completado y guardado en PowerBI/insight_openai.txt")
