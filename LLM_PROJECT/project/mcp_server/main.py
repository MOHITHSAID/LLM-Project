from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Hotel Tool
# -------------------------

class HotelRequest(BaseModel):
    location: str

@app.post("/hotels")
def get_hotels(req: HotelRequest):
    return {
        "location": req.location,
        "hotels": [
            {"name": "Hotel Taj View", "rating": 4.5},
            {"name": "Agra Residency", "rating": 4.2}
        ]
    }

# -------------------------
# Transport Tool
# -------------------------

class TransportRequest(BaseModel):
    source: str
    destination: str

@app.post("/transport")
def get_transport(req: TransportRequest):
    return {
        "route": f"{req.source} → {req.destination}",
        "options": [
            {"type": "Train", "duration": "2 hours"},
            {"type": "Bus", "duration": "3 hours"},
            {"type": "Cab", "duration": "1.5 hours"}
        ]
    }

# -------------------------
# Traffic Tool
# -------------------------

class TrafficRequest(BaseModel):
    location: str

@app.post("/traffic")
def get_traffic(req: TrafficRequest):
    return {
        "location": req.location,
        "status": "Moderate traffic",
        "delay": "15 minutes"
    }
