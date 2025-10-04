import requests
from typing import Optional
from logger import frontend_logger

class LLMService:
    def __init__(self):
        self.api_url = "0.0.0.0"
        self.api_port = 8000

    @staticmethod
    def _make_request(url: str, prompt_params: dict) -> Optional[requests.Response]:
        try:
            response = requests.get(url, params=prompt_params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            frontend_logger.error(f"Request to {url} failed: {e}")
            return None
        
    def get_prompt_response(self, prompt: str) -> Optional[str]:
        url = f"http://{self.api_url}:{self.api_port}/prompt"
        prompt_params = {"prompt": prompt}
        response = self._make_request(url, prompt_params=prompt_params)
        if response:
            try:
                data = response.json()
                return data.get("response")
            except ValueError as e:
                frontend_logger.error(f"Failed to parse JSON response: {e}")
        return None
    