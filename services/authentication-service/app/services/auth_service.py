from sqlalchemy.orm import Session
from models.user import User
from utils.password_utils import hash_password, verify_password
from utils.jwt_utils import create_access_token, verify_token
from fastapi import Depends, HTTPException
import jwt
import os



def register_user(db: Session, username: str, email: str, password: str, role: str):
    hashed_pw = hash_password(password)
    new_user = User(username=username, email=email, password=hashed_pw, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def generate_token(user: User):
    return create_access_token({"sub": user.username, "role": user.role})


def require_role(required_role: str):
    def role_checker(user_data=Depends(verify_token)):
        if user_data["role"] != required_role:
            raise HTTPException(status_code=403, detail="Access denied")
        return user_data
    return role_checker
