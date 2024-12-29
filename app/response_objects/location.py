from pydantic import BaseModel


class LocationResponse(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
