from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateReviewRequest(BaseModel):
    location_id: int
    category_id: int
    review_date: Optional[datetime] = None


class UpdateReviewRequest(BaseModel):
    location_id: Optional[int] = None
    category_id: Optional[int] = None
    review_date: Optional[datetime] = None
