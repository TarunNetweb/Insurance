from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from config.database import engine
from models.user import Base

app = FastAPI(title="Auth Service")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Auth Service is running"}
