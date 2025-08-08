# Junction Table between promotions and menu items

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PromotionMenuItem(Base):
    __tablename__ = "promotion_menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))

    promotion = relationship("Promotion", back_populates="menu_items")
    sandwich = relationship("Sandwich", back_populates="promotions")

# Comment added

