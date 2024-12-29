from repositories.database import DatabaseRepository
from database.review import Review

from sqlalchemy import desc, func
from datetime import datetime, timedelta, timezone


class ExplorationUseCase:
    def __init__(self, db_repo: DatabaseRepository):
        self.__db_repo = db_repo

    def execute(self, db_item_base: type[Review]) -> list[Review]:
        thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)
        session = self.__db_repo.get_session()
        query = (
            session.query(db_item_base)
            .filter(
                (Review.review_date == None) | (Review.review_date < thirty_days_ago)
            )
            .order_by(
                func.coalesce(Review.review_date, datetime(1970, 1, 1)),
                desc(Review.review_date),
            )
            .limit(10)
        ).all()

        return query
