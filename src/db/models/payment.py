
# ============================================================================
# FILE: src/db/models/payment.py
# ============================================================================
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, DateTime, Enum,String
from src.db.base import Base
from datetime import datetime
import enum

class PaymentMethodEnum(str, enum.Enum):
    CASH = "Cash"
    CARD = "Card"
    UPI = "UPI"

class PaymentStatusEnum(str, enum.Enum):
    PAID = "Paid"
    REFUNDED = "Refunded"
    PENDING = "Pending"

class Payment(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    method = Column(Enum(PaymentMethodEnum), nullable=False)
    status = Column(Enum(PaymentStatusEnum), default=PaymentStatusEnum.PENDING)
    transaction_id = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Payment(payment_id={self.payment_id}, amount={self.amount})>"
