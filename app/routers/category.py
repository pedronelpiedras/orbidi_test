from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.core import get_db
from repositories.database import DatabaseRepository
from database.category import Category
from request_objects.category import CategoryRequest
from response_objects.category import CategoryResponse
from utils.exception_handler import exception_handler


categories_router = APIRouter(
    prefix="/categories",
)


@categories_router.post("/")
@exception_handler
def create_category(
    _: Request,
    category_request: CategoryRequest,
    database: Session = Depends(get_db),
) -> CategoryResponse:
    db_repo = DatabaseRepository(database)
    category = db_repo.create_db_item(category_request, Category)
    return CategoryResponse(**category.__dict__)


@categories_router.get("/")
@exception_handler
def get_locations(
    _: Request,
    database: Session = Depends(get_db),
) -> list[CategoryResponse]:
    db_repo = DatabaseRepository(database)
    categories = db_repo.get_items(Category)
    return [CategoryResponse(**item.__dict__) for item in categories]


@categories_router.get("/{category_id}")
@exception_handler
def get_category(
    _: Request, category_id: int, database: Session = Depends(get_db)
) -> CategoryResponse:
    db_repo = DatabaseRepository(database)
    category = db_repo.read_db_item(category_id, Category)
    return CategoryResponse(**category.__dict__)


@categories_router.put("/{category_id}")
@exception_handler
def update_category(
    _: Request,
    category_id: int,
    category_request: CategoryRequest,
    database: Session = Depends(get_db),
) -> CategoryResponse:
    db_repo = DatabaseRepository(database)
    category = db_repo.update_db_item(category_id, category_request, Category)
    return CategoryResponse(**category.__dict__)


@categories_router.delete("/{category_id}")
@exception_handler
def delete_category(
    _: Request, category_id: int, database: Session = Depends(get_db)
) -> CategoryResponse:
    db_repo = DatabaseRepository(database)
    category = db_repo.delete_db_item(category_id, Category)
    return CategoryResponse(**category.__dict__)
