from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReviewRequest(BaseModel):
    location_id: int
    category_id: int
    review_date: Optional[datetime] = None
