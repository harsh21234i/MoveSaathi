from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.driver_service import register_driver_service

router = APIRouter(tags=["Driver"])


@router.post("/driver/register")
def register_driver(
    name: str,
    email: str,
    password: str,
    vehicle_type: str,
    db: Session = Depends(get_db)
):
    return register_driver_service(db, name, email, password, vehicle_type)