import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.category import Category
from database.location import Location
from database.review import Review
from database.base import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

ENGINE = create_engine(DATABASE_URL)
SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
Base.metadata.create_all(bind=ENGINE)


class NotFoundError(Exception):
    pass


def get_db():
    database = SESSION_LOCAL()
    try:
        yield database
    finally:
        database.close()
