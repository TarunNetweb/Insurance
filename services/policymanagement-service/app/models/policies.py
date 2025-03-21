# models/policies.py
from sqlalchemy import Column, Integer, String, DateTime, func
from config.database import Base

class PolicyDocument(Base):
    __tablename__ = "policy_documents"

    id = Column(Integer, primary_key=True, index=True)
    pdf_path = Column(String(255), nullable=False)
    text_content = Column(String, nullable=True)
    user_name = Column(String(100), nullable=False)
    user_role = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

class PolicyActivity(Base):
    __tablename__ = "policy_activity"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String(50), nullable=False)
    file_name = Column(String(255), nullable=False)
    user_name = Column(String(100), nullable=False)
    user_role = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=func.now())
