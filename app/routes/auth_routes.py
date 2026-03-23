from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database.connection import get_db
from app.schemas.user_schema import UserCreate
from app.services.auth_service import register_user_service, login_user_service

router = APIRouter(tags=["Authentication"])


@router.post("/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user_service(db, user)


@router.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user_service(db, form_data.username, form_data.password)