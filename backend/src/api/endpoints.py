from fastapi import APIRouter
from services.llm import LLMService
from logger import backend_logger
from typing import Optional

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/prompt")
async def prompt_user(prompt: str) -> dict[str, Optional[str]]:
    llm_service = LLMService()
    response = llm_service.generate_text(prompt)
    if not response:
        backend_logger.error("LLM service returned no response.")
        return {"response": None}
    return {"response": response}
