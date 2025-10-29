import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router
from config.settings import settings
from cloud_storage import StorageManager

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

def main():
    storage_manager = StorageManager()
    storage_manager.download_all_from_datahub()
    

if __name__ == "__main__":
    main()
    uvicorn.run(app, host=settings.host, port=settings.port)
