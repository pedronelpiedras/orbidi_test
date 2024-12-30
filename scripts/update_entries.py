import requests
from pprint import pprint
from datetime import datetime, timezone

now = datetime.now(timezone.utc)

ITERATIONS = 40


for i in range(ITERATIONS):
    pprint(
        requests.put(
            f"http://127.0.0.1:8000/categories/{i+1}",
            json={"name": f"updated_category_{i}"},
        ).json()
    )

for i in range(ITERATIONS):
    pprint(
        requests.put(
            f"http://127.0.0.1:8000/locations/{i+1}",
            json={"name": f"updated_location_{i}"},
        ).json()
    )
for i in range(ITERATIONS):
    pprint(
        requests.put(
            f"http://127.0.0.1:8000/reviews/{i+1}", json={"review_date": str(now)}
        ).json()
    )
