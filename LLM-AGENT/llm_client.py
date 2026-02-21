# llm_client.py

from google import genai
from config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)