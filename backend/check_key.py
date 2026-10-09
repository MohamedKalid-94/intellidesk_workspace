import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model=os.environ.get("LLM_MODEL", "gemini-3.5-flash-lite"),
    contents="Say I'm not Dangerous Skyler in one word",
)
print(response.text)