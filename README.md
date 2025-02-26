# MySite Blog

A Django-powered blog application with tagging, comments, and RSS feed capabilities.

## Live Demo

The application is deployed on Render: [https://mysite-m.onrender.com](https://mysite-m.onrender.com/blog/home.html)

## Features

- Responsive design with custom CSS
- Blog posts with Markdown support
- Tagging system (using django-taggit)
- Comment system
- RSS feed for blog posts
- Pagination
- Admin interface for content management
- Sitemap generation

## Tech Stack

- Python 3.11
- Django 5.1.6
- PostgreSQL (in production)
- SQLite (in development)
- Markdown for content formatting
- Gunicorn for production server
- Whitenoise for static files
- Uvicorn as ASGI server
- HTML, CSS, JavaScript



## Project Structure

# Short:

```
mysite_m/
├── account/              # User account management
│   ├── _pycache_/        # Python bytecode cache
│   ├── migrations/       # Database migrations
│   ├── static/           # Static files for account
│   ├── templates/        # HTML templates
│   │   ├── account/      # Account-specific templates
│   │   └── registration/ # Registration templates
│   │  
├── blog/                 # Main blog application
│   ├── _pycache_/        # Python bytecode cache
│   ├── migrations/       # Database migrations
│   ├── static/blog_static # Static files (CSS, images)
│   │   ├── css/          # Stylesheets
│   │   └── images/       # Images
│   ├── templates/        # HTML templates
│   │   └── blog/         # Blog-specific templates
│   │       └── comment/  # Comment templates
│   │ 
│   └── templatetags/     # Custom template tags
│   
├── mysite/               # Project settings
│   
└── staticfiles/          # Collected static files

# Or detailed:
mysite_m/
├── account/              # User account management
│   ├── _pycache_/        # Python bytecode cache
│   ├── migrations/       # Database migrations
│   ├── static/           # Static files for account
│   ├── templates/        # HTML templates
│   │   ├── account/      # Account-specific templates
│   │   ├── registration/ # Registration templates
│   │   └── base_1.html   # Base template for account
│   ├── __init__.py       # Package initialization
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # App configuration
│   ├── authentication.py # Authentication handlers
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── tests.py          # Test cases
│   ├── urls.py           # URL routing
│   └── views.py          # View functions
├── blog/                 # Main blog application
│   ├── _pycache_/        # Python bytecode cache
│   ├── migrations/       # Database migrations
│   ├── static/blog_static # Static files (CSS, images)
│   │   ├── css/          # Stylesheets
│   │   └── images/       # Images
│   ├── templates/        # HTML templates
│   │   └── blog/         # Blog-specific templates
│   │       ├── comment/  # Comment templates
│   │       ├── post/     # Post templates
│   │       ├── base.html # Base template
│   │       ├── home.html # Homepage template
│   │       └── pagination.html # Pagination component
│   ├── templatetags/     # Custom template tags
│   ├── __init__.py       # Package initialization
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # App configuration
│   ├── feeds.py          # RSS feed implementation
│   ├── forms.py          # Form definitions
│   ├── models.py         # Database models
│   ├── sitemaps.py       # Sitemap generation
│   ├── tests.py          # Test cases
│   ├── urls.py           # URL routing
│   └── views.py          # View functions
├── mysite/               # Project settings
│   ├── _pycache_/        # Python bytecode cache
│   ├── __init__.py       # Package initialization
│   ├── .env              # Environment variables
│   ├── asgi.py           # ASGI configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── staticfiles/          # Collected static files
├── .env                  # Root environment variables
├── .gitignore            # Git ignore file
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── mysite_data.json      # Data export/backup
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```



## Installation

1. Clone the repository:
```bash
git clone https://github.com/konmez/mysite_m.git
cd mysite_m
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

The site will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment

This project is configured for deployment on Render. Key deployment settings include:

- `ALLOWED_HOSTS` configured for Render domains
- PostgreSQL database connection via `dj-database-url`
- Static files served with Whitenoise
- Gunicorn as the WSGI server

## Environment Variables for Production

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Kon Mez

## Acknowledgements

- Django documentation
- Django blog tutorial by [Antonio Melé](https://github.com/amele/django-by-example-book)
- LoveRunning project by [Code Institute](8.1-testing-and-validation)
- Render for hosting services
