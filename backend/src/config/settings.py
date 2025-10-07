from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

class BackendSettings(BaseSettings):
    app_name: str = Field("HK Housing Agent Backend")
    app_description: str = Field("Backend service for HK Housing Agent")
    app_version: str = Field("1.0.0")
    host: str = Field("0.0.0.0")
    port: int = Field(8000)
    
    openrouter_api_url: str = Field(...)
    openrouter_api_key: str = Field(...)
    openrouter_model: str = Field("meta-llama/llama-3.3-8b-instruct:free")
    
    llm_max_tokens: int = Field(1024)
    
    model_config = SettingsConfigDict(
        env_file=Path(os.getenv("ENV_FILE", ".env")),
        env_file_encoding="utf-8",
        case_sensitive=False,
        )
    

settings = BackendSettings()
