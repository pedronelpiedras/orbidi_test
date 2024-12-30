To setup this project one needs to have docker and python3.13 installed

Steps:
 - unzip orbidi_test-main
 - In a terminal go into the folder
 - create a virtual env
 - activate virtual env
 - run 'pip install -r requirements.txt'
 - run 'docker compose up'
 - go into a diferent terminal into the same folder, activate the virtual env
 - run 'pip install requests'
 - run 'python ./scripts/create_entries.py' to create locations, categories and location_categories_reviewed
 - in the same terminal run 'python ./scripts/get_entries.py' to get 10 recomended location-category entries
