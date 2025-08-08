from datetime import datetime
from pydantic import BaseModel

class PaymentBase(BaseModel):
    payment_type: str
    card_number: str
    status: str
    amount: float

class PaymentCreate(PaymentBase):
    order_id: int

class Payment(PaymentBase):
    id: int
    order_id: int
    timestamp: datetime

    class ConfigDict:
        from_attributes = True