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
from database.location import Location
from request_objects.location import CreateLocationRequest, UpdateLocationRequest
from response_objects.location import LocationResponse


locations_router = APIRouter(
    prefix="/locations",
)


@locations_router.post("/")
def create_location(
    request: Request,
    location: CreateLocationRequest,
    database: Session = Depends(get_db),
) -> LocationResponse:
    db_item = create_db_item(location, Location, database)
    return LocationResponse(**db_item.__dict__)


@locations_router.get("/")
def get_locations(
    request: Request,
    database: Session = Depends(get_db),
) -> list[LocationResponse]:
    locations = get_items(Location, database)
    return [LocationResponse(**item.__dict__) for item in locations]


@locations_router.get("/{location_id}")
def get_location(
    request: Request, location_id: int, database: Session = Depends(get_db)
) -> LocationResponse:
    try:
        db_item = read_db_item(location_id, Location, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return LocationResponse(**db_item.__dict__)


@locations_router.put("/{location_id}")
def update_location(
    request: Request,
    location_id: int,
    location: UpdateLocationRequest,
    database: Session = Depends(get_db),
) -> LocationResponse:
    try:
        db_item = update_db_item(location_id, location, Location, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return LocationResponse(**db_item.__dict__)


@locations_router.delete("/{location_id}")
def delete_location(
    request: Request, location_id: int, database: Session = Depends(get_db)
) -> LocationResponse:
    try:
        db_item = delete_db_item(location_id, Location, database)
    except NotFoundError as e:
        raise HTTPException(status_code=404) from e
    return LocationResponse(**db_item.__dict__)
