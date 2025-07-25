from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    code: str
    discount_percent: float
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True