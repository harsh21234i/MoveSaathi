from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.auth_dependency import get_current_user
from app.schemas.delivery_schema import DeliveryCreate
from app.database.connection import get_db
from app.models.delivery import Delivery

router = APIRouter(tags=["Delivery"])

@router.post("/deliveries")
def create_delivery(
    delivery: DeliveryCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    new_delivery = Delivery(
        pickup_location=delivery.pickup_location,
        drop_location=delivery.drop_location,
        package_type=delivery.package_type,
        vehicle_type=delivery.vehicle_type
    )

    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)

    return {
        "message": "Delivery created successfully",
        "delivery_id": new_delivery.id
    }


@router.get("/deliveries")
def get_deliveries(db: Session = Depends(get_db)):
    deliveries = db.query(Delivery).all()
    return deliveries