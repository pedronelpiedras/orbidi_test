import requests
from pprint import pprint

get_categories = requests.get("http://127.0.0.1:8000/categories/")
pprint(get_categories.json())

get_locations = requests.get("http://127.0.0.1:8000/locations/")
pprint(get_locations.json())

get_reviews = requests.get("http://127.0.0.1:8000/reviews/").json()
pprint(get_reviews)
