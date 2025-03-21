from sqlalchemy import Column, Integer, String, DateTime, func
from config.database import Base

class PolicyDocument(Base):
    __tablename__ = "policy_documents"

    id = Column(Integer, primary_key=True, index=True)
    pdf_url = Column(String(255), nullable=False)
    text_content = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())