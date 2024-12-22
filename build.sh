#!/bin/sh

# Install Python dependencies
pip3 install -r requirements.txt

# Install Node.js dependencies
cd theme/static_src/ 

npm install

cd .. 

cd ..

# Run Django migrations
python3 manage.py migrate

python3 manage.py tailwind start

# command to open another new terminal 
gnome-terminal --tab -- bash -c "python manage.py runserver; exec bash"