from sqlalchemy.orm import Session
from app.models.delivery import Delivery
from app.schemas.delivery_schema import DeliveryCreate


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