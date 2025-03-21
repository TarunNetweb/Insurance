from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from services.policy_service import process_pdf, upload_policy, update_policy, delete_policy
from config.database import get_db
from utils.jwt_utils import require_admin_role, verify_token

router = APIRouter()

@router.post("/process-pdf/")
def process_pdf_route(bucket_name: str, blob_name: str, db: Session = Depends(get_db), user_data=Depends(verify_token)):
    return process_pdf(db, bucket_name, blob_name, user_data)

@router.post("/upload-policy/")
def upload_policy_route(bucket_name: str, file: UploadFile = File(...), db: Session = Depends(get_db), user_data=Depends(verify_token), admin=Depends(require_admin_role)):
    return upload_policy(db, bucket_name, file, user_data)

@router.put("/update-policy/{policy_id}")
def update_policy_route(policy_id: int, bucket_name: str, file: UploadFile = File(...), db: Session = Depends(get_db), user_data=Depends(verify_token), admin=Depends(require_admin_role)):
    return update_policy(db, policy_id, bucket_name, file, user_data)

@router.delete("/delete-policy/{policy_id}")
def delete_policy_route(policy_id: int, bucket_name: str, db: Session = Depends(get_db), user_data=Depends(verify_token), admin=Depends(require_admin_role)):
    return delete_policy(db, policy_id, bucket_name, user_data)