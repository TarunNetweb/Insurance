from fastapi import FastAPI
from routes.policy_routes import router
from config.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Policy Management Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Policy Management Service is Running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8500)