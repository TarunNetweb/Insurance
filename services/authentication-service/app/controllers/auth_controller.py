from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.auth_service import register_user, authenticate_user, generate_token
from config.database import get_db
from models.schemas import UserRegisterRequest, UserLoginRequest

router = APIRouter()

@router.post("/signup")
def signup(request: UserRegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, request.username, request.email, request.password)
    return {"message": "User created successfully", "user_id": user.id}

@router.post("/login")
def login(request: UserLoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = generate_token(user)
    return {"access_token": token, "token_type": "bearer"}
