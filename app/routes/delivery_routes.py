from fastapi import APIRouter
from app.schemas.delivery_schema import DeliveryCreate

router = APIRouter()

deliveries = []

@router.post("/deliveries")
def create_delivery(delivery: DeliveryCreate):
    deliveries.append(delivery)
    return {
        "message": "Delivery created successfully",
        "delivery": delivery
    }

@router.get("/deliveries")
def get_deliveries():
    return deliveries