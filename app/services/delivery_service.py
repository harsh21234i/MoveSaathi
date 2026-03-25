from sqlalchemy.orm import Session
from app.models.delivery import Delivery
from app.schemas.delivery_schema import DeliveryCreate
from fastapi import HTTPException

def create_delivery_service(db: Session, delivery: DeliveryCreate, user_id: int):
    new_delivery = Delivery(
        pickup_location=delivery.pickup_location,
        drop_location=delivery.drop_location,
        package_type=delivery.package_type,
        vehicle_type=delivery.vehicle_type,
        user_id=user_id
    )

    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)

    return new_delivery


def get_all_deliveries_service(db: Session):
    return db.query(Delivery).all()

def accept_delivery_service(db, delivery_id: int, user):

    # check role
    if user.role != "driver":
        raise HTTPException(status_code=403, detail="Only drivers can accept deliveries")

    # check availability
    if not user.is_available:
        raise HTTPException(status_code=400, detail="Driver is offline")

    delivery = db.query(Delivery).filter(Delivery.id == delivery_id).first()

    if not delivery:
        raise HTTPException(status_code=404, detail="Delivery not found")

    if delivery.status != "pending":
        raise HTTPException(status_code=400, detail="Delivery already accepted")

    # assign driver
    delivery.driver_id = user.id
    delivery.status = "accepted"

    db.commit()
    db.refresh(delivery)

    return {
        "message": "Delivery accepted successfully",
        "delivery_id": delivery.id,
        "driver_id": user.id
    }

def get_available_deliveries_service(db):
    deliveries = db.query(Delivery).filter(Delivery.status == "pending").all()

    response = []
    for d in deliveries:
        response.append({
            "id": d.id,
            "pickup": d.pickup_location,
            "drop": d.drop_location,
            "vehicle": d.vehicle_type,
            "status": d.status
        })

    return response