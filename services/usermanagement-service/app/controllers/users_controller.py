from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.users_services import delete_user, update_user
from config.database import get_db
from utils.jwt_utils import require_admin_role
from models.schemas import UpdateUserRequest
router = APIRouter()


@router.delete("/delete/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db),admin=Depends(require_admin_role)):
    return delete_user(db, user_id)

@router.put("/update/{user_id}")
def update_user_route(user_id: int, request: UpdateUserRequest, db: Session = Depends(get_db),
                    admin=Depends(require_admin_role)):
    return update_user(db, user_id, request.username, request.email, request.first_name, request.last_name, request.phone_number,request.password)
