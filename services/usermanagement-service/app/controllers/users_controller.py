from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.users_services import delete_user, update_user, get_all_users,search_an_user,update_user_own_profile
from config.database import get_db
from typing import List, Optional
from utils.jwt_utils import require_admin_role, verify_token
from models.schemas import UpdateUserRequest
router = APIRouter()


@router.delete("/delete/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db),admin=Depends(require_admin_role)):
    return delete_user(db, user_id)

@router.put("/update/{user_id}")
def update_user_route(user_id: int, request: UpdateUserRequest, db: Session = Depends(get_db),
                    admin=Depends(require_admin_role)):
    return update_user(db, user_id, request.username, request.email, request.first_name, request.last_name, request.phone_number,request.password)

@router.put("/updateown")
def update_user_route(
    request: UpdateUserRequest, 
    db: Session = Depends(get_db), 
    user_data=Depends(verify_token)):
    return update_user_own_profile(db, user_data["username"], request)

@router.get("/userlist")
def get_all_users_route(db: Session = Depends(get_db), admin=Depends(require_admin_role)):
    return get_all_users(db)


@router.get("/search_user")
def search_users( first_name: Optional[str] = None, email: Optional[str] = None, 
                 username: Optional[str] = None, db: Session = Depends(get_db)):
    
    return search_an_user(db, first_name, email, username)