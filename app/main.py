from fastapi import FastAPI
from app.routes import delivery_routes

app = FastAPI(title="MoveSaathi Delivery API")
app.include_router(delivery_routes.router)
@app.get("/")
def home():
    return{"message": "movesaathi backend running"}