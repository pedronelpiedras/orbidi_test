from fastapi import FastAPI
from routers.location import locations_router
from routers.category import categories_router
from routers.review import reviews_router


app = FastAPI()

app.include_router(locations_router)
app.include_router(categories_router)
app.include_router(reviews_router)


@app.get("/")
def read_root():
    return "Server is running."
