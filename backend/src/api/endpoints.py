from fastapi import APIRouter
from services.llm import LLMService

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/echo")
async def echo(message: str):
    return {"message": message}

@router.get("/prompt")
async def prompt_user(prompt: str):
    llm_service = LLMService()
    response = llm_service.generate_text(prompt)
    return {"response": response}
