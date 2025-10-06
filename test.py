import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    openai.models.list()
    print("✅ API key is valid")
except Exception as e:
    print("❌ Invalid API key:", e)
