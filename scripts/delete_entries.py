import requests
from pprint import pprint

ITERATIONS = 40

for i in range(ITERATIONS):
    pprint(requests.delete(f"http://127.0.0.1:8000/categories/{i+1}").json())

for i in range(ITERATIONS):
    pprint(requests.delete(f"http://127.0.0.1:8000/locations/{i+1}").json())
for i in range(ITERATIONS):
    pprint(requests.delete(f"http://127.0.0.1:8000/reviews/{i+1}").json())
