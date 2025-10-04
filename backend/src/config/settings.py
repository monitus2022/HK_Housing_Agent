from pydantic import BaseModel, Field

class BackendSettings(BaseModel):
    app_name: str = Field("HK Housing Agent Backend", env="APP_NAME")
    app_description: str = Field("Backend service for HK Housing Agent", env="APP_DESCRIPTION")
    app_version: str = Field("1.0.0", env="APP_VERSION")
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = BackendSettings()