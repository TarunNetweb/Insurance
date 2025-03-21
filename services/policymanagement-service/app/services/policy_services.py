import fitz
from sqlalchemy.orm import Session
from models.policies import PolicyDocument
from fastapi import HTTPException, UploadFile
from utils.cloud_storage import download_pdf_from_gcs, upload_pdf_to_gcs, delete_pdf_from_gcs

def process_pdf(db: Session, bucket_name: str, blob_name: str):
    pdf_path = download_pdf_from_gcs(bucket_name, blob_name)
    doc = fitz.open(pdf_path)

    extracted_text = ""
    contains_images = False

    for page in doc:
        images = page.get_images(full=True)
        if images:
            contains_images = True
            break
        extracted_text += page.get_text("text")

    if contains_images:
        raise HTTPException(status_code=400, detail="PDF contains images or non-text elements")

    policy_doc = PolicyDocument(pdf_url=blob_name, text_content=extracted_text)
    db.add(policy_doc)
    db.commit()
    db.refresh(policy_doc)

    with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

    return {"message": "PDF processed successfully", "document_id": policy_doc.id}

def upload_policy(db: Session, bucket_name: str, file: UploadFile):
    blob_name = upload_pdf_to_gcs(bucket_name, file)
    return {"message": "Policy uploaded successfully", "blob_name": blob_name}

def update_policy(db: Session, policy_id: int, bucket_name: str, file: UploadFile):
    delete_pdf_from_gcs(bucket_name, policy_id)
    blob_name = upload_pdf_to_gcs(bucket_name, file)
    return {"message": "Policy updated successfully", "blob_name": blob_name}

def delete_policy(db: Session, policy_id: int, bucket_name: str):
    delete_pdf_from_gcs(bucket_name, policy_id)
    return {"message": "Policy deleted successfully"}
