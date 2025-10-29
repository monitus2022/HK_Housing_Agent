from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Literal, Optional


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

    cloud_storage_access_key_id: str = Field(...)
    cloud_storage_secret_access_key: str = Field(...)
    cloud_storage_bucket_name: str = Field(...)
    cloud_storage_bucket_region: str = Field(default="auto")

    cloud_storage_service_type: Literal["cloudflare", "aws"] = Field(
        default="cloudflare", description="Type of cloud storage service to use"
    )
    cloudflare_account_id: Optional[str] = Field(
        None, description="Cloudflare R2 Account ID, leave empty if using AWS S3"
    )
    cloudflare_endpoint_template: Optional[str] = Field(
        None, description="Cloudflare R2 Endpoint URL template, leave empty if using AWS S3"
    )
    aws_endpoint_template: Optional[str] = Field(
        None, description="AWS S3 Endpoint URL template, leave empty if using Cloudflare R2"
    )
    
    cloudflare_datahub_folder_name: str = Field(
        "data", description="Folder name in Cloudflare R2 bucket for datahub files"
    )

    local_data_folder_path: str = Field(
        "data", description="Local path to store data files"
    )

    # Combine endpoint specific info
    @property
    def cloudflare_endpoint_url(self) -> Optional[str]:
        if self.cloudflare_account_id and self.cloudflare_endpoint_template:
            return self.cloudflare_endpoint_template.format(
                cloudflare_account_id=self.cloudflare_account_id
            )
        return None

    @property
    def aws_endpoint_url(self) -> Optional[str]:
        if self.cloud_storage_bucket_region and self.aws_endpoint_template:
            return self.aws_endpoint_template.format(
                bucket_region=self.cloud_storage_bucket_region
            )
        return None

    model_config = SettingsConfigDict(case_sensitive=False)


settings = BackendSettings()
