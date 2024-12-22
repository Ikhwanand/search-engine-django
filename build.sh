#!/bin/sh

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files if needed (optional)
python manage.py collectstatic --noinput

# Build your Django app (if needed, e.g., using a bundler or custom build process)
python manage.py tailwind start

# Run the Django development server
python manage.py runserver