from sqlalchemy.orm import Session
from models.users import User
from fastapi import HTTPException
from utils.password_utils import hash_password
def delete_user(db: Session, user_id: int):
    """Deletes a user from the database."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

def update_user(db: Session, user_id: int, username: str = None, email: str = None, 
                first_name:  str = None,last_name:  str = None, phone_number: str = None, password: str = None):
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if username:
        user.username = username
    if email:
        user.email = email
    if last_name:
        user.last_name = last_name
    if first_name:
        user.first_name = first_name
    if phone_number:
        user.phone_number = phone_number
    if password:
        user.password = hash_password(password)
        

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": {"id": user.id, "username": user.username, "email": user.email}}
