from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class FrontendSettings(BaseSettings):
    app_name: str = Field("HK Housing Agent Chatbot")
    app_description: str = Field("Chatbot service for HK Housing Agent")
    
    backend_url: str = Field()
    backend_port: int = Field(8000)
    backend_prompt_endpoint: str = Field("/prompt")
    
    model_config = SettingsConfigDict(case_sensitive=False)
    

settings = FrontendSettings()
