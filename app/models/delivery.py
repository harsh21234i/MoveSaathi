from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    pickup_location = Column(String)
    drop_location = Column(String)
    package_type = Column(String)
    vehicle_type = Column(String)
    status = Column(String, default="pending")
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=True)