from sqlalchemy import Column, Integer, String, Boolean
from app.models.delivery import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    vehicle_type = Column(String, nullable=True)
    is_available = Column(Boolean, default=False)