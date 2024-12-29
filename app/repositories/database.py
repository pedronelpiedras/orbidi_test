from sqlalchemy.orm import Session
from database.base import BaseSubClass_co, BaseModelSubClass_co
from database.core import NotFoundError


class DatabaseRepository:
    """This class has some basic db operation one can use.
    If one needs a custom query one should get the db session with the get_session method
    """

    def __init__(self, session: Session):
        self.__session = session

    def get_items(self, db_item_base: type[BaseSubClass_co]) -> list[BaseSubClass_co]:
        return self.__session.query(db_item_base).limit(10).all()

    def read_db_item(
        self, item_id: int, db_item_base: type[BaseSubClass_co]
    ) -> BaseSubClass_co:
        db_item = (
            self.__session.query(db_item_base)
            .filter(db_item_base.id == item_id)
            .first()
        )
        if db_item is None:
            raise NotFoundError(f"Item with id {item_id} not found.")
        return db_item

    def create_db_item(
        self, item: BaseModelSubClass_co, db_item_base: type[BaseSubClass_co]
    ) -> BaseSubClass_co:
        db_item = db_item_base(**item.model_dump(exclude_none=True))
        self.__session.add(db_item)
        self.__session.commit()
        self.__session.refresh(db_item)

        return db_item

    def update_db_item(
        self,
        item_id: int,
        item: BaseModelSubClass_co,
        db_item_base: type[BaseSubClass_co],
    ) -> BaseSubClass_co:
        db_item = self.read_db_item(item_id, db_item_base)
        for key, value in item.model_dump(exclude_none=True).items():
            setattr(db_item, key, value)
        self.__session.commit()
        self.__session.refresh(db_item)
        return db_item

    def delete_db_item(
        self, item_id: int, db_item_base: type[BaseSubClass_co]
    ) -> BaseSubClass_co:
        db_item = self.read_db_item(item_id, db_item_base)
        self.__session.delete(db_item)
        self.__session.commit()
        return db_item

    def get_session(self) -> Session:
        return self.__session
