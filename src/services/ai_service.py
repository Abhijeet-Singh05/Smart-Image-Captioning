import google.generativeai as genai
import json
from src.config import config
from src.utils.api_error import apiError

# configure the AI with key
genai.configure(api_key=config.GEMINI_API_KEY)

async def generate_caption(image_bytes: bytes, mime_type: str):
    try:
        model = genai.GenerativeModel('gemini-flash-latest')

        prompt = """ You are a social media expert. Analyze this image.
        1. Write an engaging Instagram caption (max 2 sentences).
        2. Create 5 trending hashtags.
        3. OUTPUT FORMAT: Return ONLY valid JSON:
        { "caption": "your text", "hashtags": ["#tag1", "#tag2"] } """
             
        response = await model.generate_content_async([
            {
                'mime_type': mime_type,
                'data': image_bytes
            },
            prompt
        ])

        clean_text = response.text.replace("```json","").replace("```","").strip()

        return json.loads(clean_text)
    
    except Exception as e:
        raise apiError(500,"AI Service is down",errors=[str(e)])