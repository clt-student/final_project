from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    promotion = relationship("Promotion", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)