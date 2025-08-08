from pydantic import BaseModel

class PromotionMenuItemBase(BaseModel):
    promotion_id: int
    sandwich_id: int

class PromotionMenuItemCreate(PromotionMenuItemBase):
    pass

class PromotionMenuItem(PromotionMenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True
