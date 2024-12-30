To setup this project one needs to have docker and python3.13 installed

Steps:
 - unzip orbidi_test-main.
 - In a terminal go into the folder.
 - create a virtual env.
 - activate virtual env.
 - run 'pip install -r requirements.txt'.
 - run 'docker compose up'.
 - go into a diferent terminal into the same folder, activate the virtual env.
 - run 'pip install requests'.
 - run 'python ./scripts/create_entries.py' to create locations, categories and location_categories_reviewed.
 - in the same terminal run 'python ./scripts/get_entries.py' to get 10 recomended location-category entries.
 - you can also run 'python ./scripts/get_entries.py' to update all entries or 'python ./scripts/delete_entries.py' to delete them.

Future Upgrades:
 - This uses currently a sqlite db. With more time one'd use a different sql engine.
 - The documentation could improve, adding better descriptions, examples, etc.
 - Add an index to the review_date column in the table 'location_category_reviewed'.
 - Add a redis cache and store the get exploration reviews result in it, invalidating the cache whenever a new review gets added.
 - Add unit tests.
 - General tweaks.
