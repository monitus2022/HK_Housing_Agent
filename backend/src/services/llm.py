from config.settings import settings
from openai import OpenAI
from logger import backend_logger
from typing import Optional

class LLMService:
    def __init__(self):
        self.api_key = settings.openrouter_api_key
        if not self.api_key:
            backend_logger.error("OpenRouter API key is not set.")
            raise ValueError("OpenRouter API key is required")
        
        self.client = OpenAI(
            base_url=settings.openrouter_api_url,
            api_key=self.api_key
            )

    def generate_text(self, prompt: str) -> Optional[str]:
        response = self.client.chat.completions.create(
            model=settings.openrouter_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=settings.llm_max_tokens,
        )
        if not response.choices or not response.choices[0].message:
            backend_logger.error("No response from LLM")
            return None
        return response.choices[0].message.content
