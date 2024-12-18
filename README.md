# Django Search Engine

A web-based search engine built with Django and styled with Tailwind CSS. This application allows users to search the web, save bookmarks, and maintain search history.

## Features

- 🔍 Web Search functionality
- 🔐 User Authentication (Login/Register)
- 📚 Bookmark Management
- 📝 Search History Tracking
- 🎨 Modern UI with Tailwind CSS
- 📱 Responsive Design
- 🔑 Password Reset Functionality


## Technologies Used

- Django
- Tailwind CSS
- Django-allauth (Authentication)
- SQLite Database
- Django Browser Reload

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd search-engine-django
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Create a `.env` file in the root directory
   - Add the following variables:
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Install and build Tailwind CSS:
```bash
python manage.py tailwind install
python manage.py tailwind build
```

7. Create a superuser (admin):
Using a direct management command:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.get(username='your_superuser_name').delete()"
```
and then see all superusers first:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True))"
```
after that, create a new superuser with your version:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
   - Main application: http://127.0.0.1:8000
   - Admin interface: http://127.0.0.1:8000/admin

## Project Structure

```
search-engine-django/
├── core/                   # Project settings and main URLs
│   ├── settings.py        # Project settings
│   └── urls.py           # Main URL configuration
├── search_engine/         # Main application
│   ├── templates/        # HTML templates
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   └── urls.py          # App URL configuration
├── theme/                # Tailwind theme configuration
├── static/              # Static files (CSS, JS, images)
└── manage.py            # Django management script
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.