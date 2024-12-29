from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReviewResponse(BaseModel):
    id: int
    location_id: int
    category_id: int
    review_date: Optional[datetime] = None
