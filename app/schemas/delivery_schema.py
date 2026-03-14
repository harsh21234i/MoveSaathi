from pydantic import BaseModel

class DeliveryCreate(BaseModel):
    pickup_location: str
    drop_location: str
    package_type: str
    vehicle_type: str