from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.utils.security import hash_password

def register_driver_service(db: Session, name: str, email: str, password: str, vehicle_type: str):

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_driver = User(
        name=name,
        email=email,
        password=hash_password(password),
        role="driver",
        vehicle_type=vehicle_type,
        is_available=True
    )

    db.add(new_driver)
    db.commit()

    return {"message": "Driver registered successfully"}

def update_driver_status_service(db, user, is_available: bool):

    # check if user is driver
    if user.role != "driver":
        raise HTTPException(status_code=403, detail="Only drivers can update status")

    # update status
    user.is_available = is_available

    db.commit()
    db.refresh(user)

    return {
        "message": f"Driver is now {'online' if is_available else 'offline'}"
    }