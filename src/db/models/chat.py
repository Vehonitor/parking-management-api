
# ============================================================================
# FILE: src/db/models/chat.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DateTime, Enum
from src.db.base import Base
from datetime import datetime
import enum

class MessageTypeEnum(str, enum.Enum):
    TEXT = "Text"
    IMAGE = "Image"
    FILE = "File"
    SYSTEM = "System"

class ChatMessage(Base):
    __tablename__ = 'chat_messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=True)
    message = Column(Text, nullable=False)
    message_type = Column(Enum(MessageTypeEnum), default=MessageTypeEnum.TEXT)
    is_read = Column(Boolean, default=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    read_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<ChatMessage(message_id={self.message_id}, sender_id={self.sender_id})>"
