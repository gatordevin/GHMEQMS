from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class AutoTQ(Base):
    __tablename__ = "autotq"
    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, unique=True, index=True, nullable=False)
    model_name = Column(String, nullable=False)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
