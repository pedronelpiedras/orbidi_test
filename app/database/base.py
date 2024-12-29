from typing import TypeVar

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)


BaseSubClass_co = TypeVar("BaseSubClass_co", bound=Base, default=Base, covariant=True)
BaseModelSubClass_co = TypeVar(
    "BaseModelSubClass_co", bound=BaseModel, default=BaseModel, covariant=True
)
