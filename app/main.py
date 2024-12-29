from fastapi import FastAPI, APIRouter
from routers.location import locations_router
from routers.category import categories_router
from routers.review import reviews_router


test_router = APIRouter()


app = FastAPI()


@test_router.get("/posts")
async def posts():
    return {"posts": "test"}


app.include_router(locations_router)
app.include_router(categories_router)
app.include_router(reviews_router)
app.include_router(test_router)


@app.get("/")
def read_root():
    return "Server is running."
