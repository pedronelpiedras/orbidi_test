from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class LocationCategoryReviewed(Base):
    __tablename__ = "location_category_reviewed"

    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    review_date: Mapped[datetime]
