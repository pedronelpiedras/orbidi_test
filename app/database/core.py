import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database.category import Category
from database.location import Location
from database.location_category_reviewed import LocationCategoryReviewed
from database.base import Base, BaseSubClass_co, BaseModelSubClass_co

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


class NotFoundError(Exception):
    pass


def get_db():
    database = session_local()
    try:
        yield database
    finally:
        database.close()


def get_items(
    db_item_base: type[BaseSubClass_co], session: Session
) -> list[BaseSubClass_co]:
    return session.query(db_item_base).all()


def read_db_item(
    item_id: int, db_item_base: type[BaseSubClass_co], session: Session
) -> BaseSubClass_co:
    db_item = session.query(db_item_base).filter(db_item_base.id == item_id).first()
    if db_item is None:
        raise NotFoundError(f"Item with id {item_id} not found.")
    return db_item


def create_db_item(
    item: BaseModelSubClass_co, db_item_base: type[BaseSubClass_co], session: Session
) -> BaseSubClass_co:
    db_item = db_item_base(**item.model_dump(exclude_none=True))
    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item


def update_db_item(
    item_id: int,
    item: BaseModelSubClass_co,
    db_item_base: type[BaseSubClass_co],
    session: Session,
) -> BaseSubClass_co:
    db_item = read_db_item(item_id, db_item_base, session)
    for key, value in item.model_dump(exclude_none=True).items():
        setattr(db_item, key, value)
    session.commit()
    session.refresh(db_item)
    return db_item


def delete_db_item(
    item_id: int, db_item_base: type[BaseSubClass_co], session: Session
) -> BaseSubClass_co:
    db_item = read_db_item(item_id, db_item_base, session)
    session.delete(db_item)
    session.commit()
    return db_item
