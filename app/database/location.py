from sqlalchemy.orm import Mapped

from database.base import Base


class Location(Base):
    __tablename__ = "locations"

    name: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
