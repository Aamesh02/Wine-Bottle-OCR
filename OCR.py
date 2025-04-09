import os
import google.generativeai as genai
from PIL import Image
from prompt import prompts

# Use environment variable for Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

def getText(image):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([
        image,
        prompts["text_prompt"]
    ])
    return response.text

def categorizeText(ocr_text):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([
        f"{prompts['format_prompt']} Below is the text extracted from the bottle:\n{ocr_text}"
    ])
    print(response.text)
    return response.text
