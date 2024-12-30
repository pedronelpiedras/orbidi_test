To setup this project one needs to have docker and python3.13 installed

Steps:
 - create a virtual env
 - activate vitual env
 - run 'pip install -r requirements.txt'
 - Go into the map_my_world folder
 - run 'docker compose up'
 - go into a diferent terminal and run 'python ./scripts/create_entries.py' to create locations, categories and location_categories_reviewed
 - in the same terminal run 'python ./scripts/get_entries.py' to get 10 recomended location-category entries
