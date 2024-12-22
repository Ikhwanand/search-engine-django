#!/bin/sh

python3 -m venv venv

source ./venv/bin/activate

# Install Python dependencies
pip3 install -r requirements.txt

pip3 install -U pip

# Install Node.js dependencies
cd theme/static_src/ 

npm install

cd .. 

cd ..

python3 manage.py makemigrations

# Run Django migrations
python3 manage.py migrate

python3 manage.py tailwind start

# command to open another new terminal 
gnome-terminal --tab -- bash -c "python3 manage.py runserver; exec bash"