import requests

get_categories = requests.get("http://127.0.0.1:8000/categories/")
print(get_categories.json())

get_locations = requests.get("http://127.0.0.1:8000/locations/")
print(get_locations.json())

get_reviews = requests.get("http://127.0.0.1:8000/reviews/").json()
print(len(get_reviews))
print(get_reviews)
