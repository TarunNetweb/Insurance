from fastapi import FastAPI
from routes.users_routes import router
from config.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "User Management Service is Running!"}
