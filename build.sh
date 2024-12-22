#!/bin/sh

#!/bin/sh

# Install Node.js dependencies and build Tailwind CSS
npm install
npx tailwindcss -i ./src/css/input.css -o ./src/css/main.css --minify

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files if needed (optional)
# python manage.py collectstatic --noinput

# Build your Django app (if needed, e.g., using a bundler or custom build process)
python manage.py tailwind start