from typing import Optional
from pydantic import BaseModel

class RatingBase(BaseModel):
    score: int
    review: Optional[str] = None

class RatingCreate(RatingBase):
    sandwich_id: int

class Rating(RatingBase):
    id: int
    sandwich_id: int

    class ConfigDict:
        from_attributes = True
