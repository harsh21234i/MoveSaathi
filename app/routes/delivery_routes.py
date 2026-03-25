from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.auth_dependency import get_current_user
from app.schemas.delivery_schema import DeliveryCreate
from app.database.connection import get_db
from app.services.delivery_service import create_delivery_service, get_all_deliveries_service, accept_delivery_service, get_available_deliveries_service
from app.utils.role_checker import check_role
from app.services.driver_service import update_driver_status_service
router = APIRouter(tags=["Delivery"])


@router.post("/deliveries")
def create_delivery(
    delivery: DeliveryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    check_role(current_user, ["customer"])

    new_delivery = create_delivery_service(db, delivery, current_user.id)

    return {
        "message": "Delivery created successfully",
        "delivery_id": new_delivery.id
    }


@router.get("/deliveries")
def get_deliveries(db: Session = Depends(get_db)):
    return get_all_deliveries_service(db)


@router.put("/driver/status")
def update_status(
    is_available: bool,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return update_driver_status_service(db, current_user, is_available)

@router.put("/deliveries/{delivery_id}/accept")
def accept_delivery(
    delivery_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return accept_delivery_service(db, delivery_id, current_user)

@router.get("/deliveries/available")
def get_available_deliveries(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    check_role(current_user, ["driver"])
    return get_available_deliveries_service(db, current_user)