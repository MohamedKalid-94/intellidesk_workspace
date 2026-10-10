import logging
from typing import Annotated

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, StringConstraints

from services.llm import complete

logger = logging.getLogger(__name__)
router = APIRouter()

Message = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=4000)]


class ChatRequest(BaseModel):
    message: Message


class ChatResponse(BaseModel):
    reply: str


@router.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    try:
        reply = complete(request.message)
    except RuntimeError:
        logger.exception("LLM request failed")
        raise HTTPException(
            status_code=503,
            detail="The AI service is temporarily unavailable. Please try again in a moment.",
        )

    if not reply:
        raise HTTPException(
            status_code=502,
            detail="The AI returned an empty response. Please rephrase and try again.",
        )
    return ChatResponse(reply=reply)