from fastapi import FastAPI
from app.routes import delivery_routes, auth_routes ,driver_routes
from app.database.connection import engine
from app.models.delivery import Base
app = FastAPI(
    title="MoveSaathi Logistics API",
    description="Backend API for MoveSaathi Delivery Platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(delivery_routes.router)
app.include_router(driver_routes.router)
@app.get("/")
def home():
    return{"message": "movesaathi backend running"}