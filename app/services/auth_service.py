from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token


def register_user_service(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role="customer"
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered successfully"}


def login_user_service(db: Session, email: str, password: str):
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"user_id": db_user.id})

    return {
        "access_token": token,
        "token_type": "bearer"
    }