from fastapi import APIRouter, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database.core import get_db
from repositories.database import DatabaseRepository
from database.location import Location
from request_objects.location import CreateLocationRequest, UpdateLocationRequest
from response_objects.location import LocationResponse
from utils.exception_handler import exception_handler


locations_router = APIRouter(
    prefix="/locations",
)


@locations_router.post("/")
@exception_handler
def create_location(
    request: Request,
    location: CreateLocationRequest,
    database: Session = Depends(get_db),
) -> LocationResponse:
    db_repo = DatabaseRepository(database)
    location = db_repo.create_db_item(location, Location, database)
    return LocationResponse(**location.__dict__)


@locations_router.get("/")
@exception_handler
def get_locations(
    request: Request,
    database: Session = Depends(get_db),
) -> list[LocationResponse]:
    db_repo = DatabaseRepository(database)
    locations = db_repo.get_items(Location, database)
    return [LocationResponse(**item.__dict__) for item in locations]


@locations_router.get("/{location_id}")
@exception_handler
def get_location(
    request: Request, location_id: int, database: Session = Depends(get_db)
) -> LocationResponse:
    db_repo = DatabaseRepository(database)
    location = db_repo.read_db_item(location_id, Location, database)
    return LocationResponse(**location.__dict__)


@locations_router.put("/{location_id}")
@exception_handler
def update_location(
    request: Request,
    location_id: int,
    location: UpdateLocationRequest,
    database: Session = Depends(get_db),
) -> LocationResponse:
    db_repo = DatabaseRepository(database)
    location = db_repo.update_db_item(location_id, location, Location, database)
    return LocationResponse(**location.__dict__)


@locations_router.delete("/{location_id}")
@exception_handler
def delete_location(
    request: Request, location_id: int, database: Session = Depends(get_db)
) -> LocationResponse:
    db_repo = DatabaseRepository(database)
    location = db_repo.delete_db_item(location_id, Location, database)
    return LocationResponse(**location.__dict__)
