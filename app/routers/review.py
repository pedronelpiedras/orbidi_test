from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.core import get_db
from repositories.database import DatabaseRepository
from database.review import Review
from request_objects.review import ReviewRequest
from response_objects.review import ReviewResponse
from use_cases.exploration import ExplorationUseCase
from utils.exception_handler import exception_handler


reviews_router = APIRouter(
    prefix="/reviews",
)


@reviews_router.post("/")
@exception_handler
def create_review(
    request: Request,
    review: ReviewRequest,
    database: Session = Depends(get_db),
) -> ReviewResponse:
    db_repo = DatabaseRepository(database)
    review = db_repo.create_db_item(review, Review, database)
    return ReviewResponse(**review.__dict__)


@reviews_router.get("/")
@exception_handler
def get_reviews(
    request: Request,
    database: Session = Depends(get_db),
) -> list[ReviewResponse]:
    db_repo = DatabaseRepository(database)
    use_case = ExplorationUseCase(db_repo)
    reviews = use_case.execute(Review)
    return [ReviewResponse(**item.__dict__) for item in reviews]


@reviews_router.get("/{review_id}")
@exception_handler
def get_review(
    request: Request, review_id: int, database: Session = Depends(get_db)
) -> ReviewResponse:
    db_repo = DatabaseRepository(database)
    review = db_repo.read_db_item(review_id, Review, database)
    return ReviewResponse(**review.__dict__)


@reviews_router.put("/{review_id}")
@exception_handler
def update_review(
    request: Request,
    review_id: int,
    review: ReviewRequest,
    database: Session = Depends(get_db),
) -> ReviewResponse:
    db_repo = DatabaseRepository(database)
    review = db_repo.update_db_item(review_id, review, Review, database)
    return ReviewResponse(**review.__dict__)


@reviews_router.delete("/{review_id}")
@exception_handler
def delete_review(
    request: Request, review_id: int, database: Session = Depends(get_db)
) -> ReviewResponse:
    db_repo = DatabaseRepository(database)
    review = db_repo.delete_db_item(review_id, Review, database)
    return ReviewResponse(**review.__dict__)
