from typing import Optional
from pydantic import BaseModel


class CreateLocationRequest(BaseModel):
    name: str
    latitude: float
    longitude: float


class UpdateLocationRequest(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
