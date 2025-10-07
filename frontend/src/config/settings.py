from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class FrontendSettings(BaseSettings):
    app_name: str = Field("HK Housing Agent Chatbot")
    app_description: str = Field("Chatbot service for HK Housing Agent")
    
    backend_url: str = Field("http://localhost")
    backend_port: int = Field(8000)
    backend_prompt_endpoint: str = Field("/prompt")
    
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False
        )
    

settings = FrontendSettings()
