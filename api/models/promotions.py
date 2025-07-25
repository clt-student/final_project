from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percent = Column(DECIMAL(4, 2), nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    # Promotions relationship
    menu_items = relationship("PromotionMenuItem", back_populates="promotion")
    orders = relationship("Order", back_populates="promotion")
