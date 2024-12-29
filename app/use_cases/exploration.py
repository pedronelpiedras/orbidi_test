from datetime import datetime, timedelta, timezone

from sqlalchemy import desc, func

from database.review import Review
from repositories.database import DatabaseRepository


class ExplorationUseCase:
    def __init__(self, db_repo: DatabaseRepository):
        self.__db_repo = db_repo

    def execute(self, db_item_base: type[Review], limit: int = 10) -> list[Review]:
        session = self.__db_repo.get_session()

        thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)
        query = (
            session.query(db_item_base)
            .filter(
                (db_item_base.review_date == None)
                | (db_item_base.review_date < thirty_days_ago)
            )
            .order_by(
                func.coalesce(db_item_base.review_date, datetime(1970, 1, 1)),
                desc(db_item_base.review_date),
            )
            .limit(limit)
        ).all()

        return query
