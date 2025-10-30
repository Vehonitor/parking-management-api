
# ============================================================================
# FILE: src/api/v1/schemas/payment.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
from src.db.models.payment import PaymentMethodEnum, PaymentStatusEnum

class PaymentBase(BaseModel):
    booking_id: int
    amount: Decimal = Field(..., ge=0, decimal_places=2)
    method: PaymentMethodEnum

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    status: PaymentStatusEnum
    transaction_id: Optional[str] = None

class PaymentResponse(PaymentBase):
    payment_id: int
    payment_date: datetime
    status: PaymentStatusEnum
    transaction_id: Optional[str] = None

    class Config:
        from_attributes = True
