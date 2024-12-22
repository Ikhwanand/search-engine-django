#!/bin/sh

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
cd theme/static_src/ 

npm install

cd .. 

cd ..

# Run Django migrations
python manage.py migrate

python manage.py tailwind start

# command to open another new terminal 
gnome-terminal --tab --title="Django" -- bash -c "python manage.py runserver; exec bash"