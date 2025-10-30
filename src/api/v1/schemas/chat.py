

# ============================================================================
# FILE: src/api/v1/schemas/chat.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.db.models.chat import MessageTypeEnum

class ChatMessageBase(BaseModel):
    receiver_id: int
    booking_id: Optional[int] = None
    message: str = Field(..., min_length=1)
    message_type: MessageTypeEnum = MessageTypeEnum.TEXT

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessageResponse(BaseModel):
    message_id: int
    sender_id: int
    receiver_id: int
    booking_id: Optional[int] = None
    message: str
    message_type: MessageTypeEnum
    is_read: bool
    sent_at: datetime
    read_at: Optional[datetime] = None

    class Config:
        from_attributes = True

