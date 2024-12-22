#!/bin/sh

# Install Python dependencies
pip install -r requirements.txt

source ./venv/bin/activate

# Run Django migrations
python manage.py migrate

# Build your Django app (if needed, e.g., using a bundler or custom build process)
python manage.py tailwind start

# Run the Django development server
python manage.py runserver