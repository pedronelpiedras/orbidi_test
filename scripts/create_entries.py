from datetime import datetime, timedelta, timezone
import requests


import random

LATITUDE_RANGE = (-180.0, 180.0)
LONGITUDE_RANGE = (-90.0, 90.0)

ITERATIONS = 40


def generate_random_datetime():

    if random.uniform(0.0, 1.0) > 0.8:
        return None
    random_seconds = random.randint(0, 60)
    random_minutes = random.randint(0, 60)
    random_hours = random.randint(0, 24)
    random_week = random.randint(0, 4)
    random_days = random.randint(0, 7)
    now = datetime.now(timezone.utc)

    # Add the random seconds to the start_date to get the random datetime
    random_datetime = now - timedelta(
        seconds=random_seconds,
        minutes=random_minutes,
        weeks=random_week,
        days=random_days,
        hours=random_hours,
    )

    return random_datetime


def create_category(name: str):
    response = requests.post(
        "http://127.0.0.1:8000/categories/",
        json={"name": name},
    )
    return response.json()


def create_location(name: str):
    response = requests.post(
        "http://127.0.0.1:8000/locations/",
        json={
            "name": name,
            "latitude": random.uniform(LATITUDE_RANGE[0], LATITUDE_RANGE[1]),
            "longitude": random.uniform(LONGITUDE_RANGE[0], LONGITUDE_RANGE[1]),
        },
    )
    return response.json()


def create_review():
    review_date = generate_random_datetime()
    response = requests.post(
        "http://127.0.0.1:8000/reviews/",
        json={
            "location_id": random.randint(0, ITERATIONS - 1),
            "category_id": random.randint(0, ITERATIONS - 1),
            "review_date": review_date if review_date is None else str(review_date),
        },
    )
    return response.json()


for i in range(ITERATIONS):
    print(create_location(f"location_{i}"))
    print(create_category(f"category_{i}"))

for i in range(ITERATIONS):
    print(create_review())
