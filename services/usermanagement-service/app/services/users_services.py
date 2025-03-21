from sqlalchemy.orm import Session
from models.users import User
from fastapi import HTTPException
from utils.password_utils import hash_password

def get_all_users(db: Session):
    try:
        return db.query(User).filter(User.role != "admin").all()
    except Exception as e:
        raise HTTPException(status_code=404, detail="Something went wrong")
    
def search_an_user(db:Session, first_name:str=None, email:str=None, username:str=None):
    try:
        query = db.query(User)
        print(" query ", query, "name email usernme",first_name,username,email)
        if first_name:
            query = query.filter(User.first_name.ilike(f"%{first_name}%"))
        if email:
            query = query.filter(User.email.ilike(f"%{email}%"))
        if username:
            query = query.filter(User.username.ilike(f"%{username}%"))
        users = query.all()
        
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        print(" query just before the sending ", query)
        return users

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

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
        
    print("user updated",user.__dict__)

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": {"id": user.id, "username": user.username, "email": user.email}}



def update_user_own_profile(db: Session, username: str, updated_data):
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        for key, value in updated_data.dict(exclude_unset=True).items():
            setattr(user, key, value)
        if updated_data.password:
            user.password = hash_password(updated_data.password)

        db.commit()
        db.refresh(user)
        return {"message": "Profile updated successfully", "user": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))