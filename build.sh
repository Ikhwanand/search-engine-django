#!/bin/sh

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Start Tailwind CSS
python manage.py tailwind start

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run the Django development server
python manage.py runserver