from pydantic import BaseModel

class PDFProcessRequest(BaseModel):
    bucket_name: str
    blob_name: str