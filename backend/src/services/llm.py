from config.settings import settings
from openai import OpenAI

class LLMService:
    def __init__(self):
        self.api_key = settings.openrouter_api_key
        self.client = OpenAI(
            base_url=settings.openrouter_api_url,
            api_key=self.api_key
            )

    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.openrouter_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
