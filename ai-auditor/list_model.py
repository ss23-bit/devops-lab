import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("📡 Querying available models...")

try:
    # Just print the names we can find
    for model in client.models.list():
        print(f"✅ Found Model: {model.name}")
except Exception as e:
    print(f"❌ Still failing: {e}")
