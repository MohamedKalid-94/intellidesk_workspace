import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_MODEL = os.environ.get("LLM_MODEL", "gemini-3.5-flash-lite")
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1024

_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def complete(prompt: str, model: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE) -> str:
    response = _client.models.generate_content(
        model=model,
        contents=prompt,
        config={"temperature": temperature, "max_output_tokens": DEFAULT_MAX_TOKENS},
    )
    return response.text