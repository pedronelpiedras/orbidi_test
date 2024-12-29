from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.core import NotFoundError, get_db
from database.core import (
    read_db_item,
    create_db_item,
    update_db_item,
    delete_db_item,
    get_items,
)
from database.category import Category
from request_objects.category import CategoryRequest
from response_objects.category import CategoryResponse


categories_router = APIRouter(
    prefix="/categories",
)


@categories_router.post("/")
def create_category(
    request: Request,
    category: CategoryRequest,
    database: Session = Depends(get_db),
) -> CategoryResponse:
    db_item = create_db_item(category, Category, database)
    return CategoryResponse(**db_item.__dict__)


@categories_router.get("/")
def get_locations(
    request: Request,
    database: Session = Depends(get_db),
) -> list[CategoryResponse]:
    categories = get_items(Category, database)
    return [CategoryResponse(**item.__dict__) for item in categories]


@categories_router.get("/{category_id}")
def get_category(
    request: Request, category_id: int, database: Session = Depends(get_db)
) -> CategoryResponse:
    try:
        db_item = read_db_item(category_id, Category, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return CategoryResponse(**db_item.__dict__)


@categories_router.put("/{category_id}")
def update_category(
    request: Request,
    category_id: int,
    category: CategoryRequest,
    database: Session = Depends(get_db),
) -> CategoryResponse:
    try:
        db_item = update_db_item(category_id, category, Category, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return CategoryResponse(**db_item.__dict__)


@categories_router.delete("/{category_id}")
def delete_category(
    request: Request, category_id: int, database: Session = Depends(get_db)
) -> CategoryResponse:
    try:
        db_item = delete_db_item(category_id, Category, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return CategoryResponse(**db_item.__dict__)
