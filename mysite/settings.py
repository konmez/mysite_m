"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import dj_database_url # type: ignore

from pathlib import Path # type: ignore

import os
from decouple import config, Config, RepositoryEnv # type: ignore



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Check if .env file exists (local development)
env_path = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_path):
    
    config = Config(RepositoryEnv(env_path))
    # Use config.get() for variables
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
    DATABASE_URL = config('DATABASE_URL')


    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')   
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

else:
    # Use os.environ for production (Render)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = (os.environ.get('DEBUG', 'False') == 'True')
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
    DATABASE_URL = os.environ.get('DATABASE_URL')

    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')   
    DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


EMAIL_PORT = 587
EMAIL_USE_TLS = True


print(f"SECRET_KEY: {SECRET_KEY}")
print(f"DEBUG: {DEBUG}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print(f"DATABASE_URL: {DATABASE_URL}")  






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'django.contrib.sites',    
    'django.contrib.sitemaps',

    'blog.apps.BlogConfig',
    'taggit',
    'django.contrib.postgres',

]


#to setup static files run following line:
# python manage.py collectstatic

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'blog', 'static'),
      
    ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': dj_database_url.parse(DATABASE_URL)
# }





# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# from decouple import config # type: ignore
# ...
# Email server configuration
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1




print(f"STATIC_ROOT: {STATIC_ROOT}")
print(f"STATICFILES_DIRS: {STATICFILES_DIRS}")
print(f"BASE_DIR: {BASE_DIR}")




# allowed_hosts_env = config('ALLOWED_HOSTS', default='').split(',')

# # Add additional required hosts
# ALLOWED_HOSTS = [
#     'mysite-qjxd.onrender.com',  # Your Render domain
#     '.render.com',
#     'localhost',
#     '127.0.0.1',
#     '127.0.0.1:8000',
# ] + [host.strip() for host in allowed_hosts_env if host.strip()]

# For debugging
print(f"Final ALLOWED_HOSTS configuration: {ALLOWED_HOSTS}")
#print(config('ALLOWED_HOSTS'))
print('DEBUG Value: >>>',DEBUG)



# Near your static files configuration
print("\nDEBUG STATIC FILES SETUP:")
print(f"BASE_DIR: {BASE_DIR}")
print(f"STATIC_ROOT: {STATIC_ROOT}")
print(f"STATICFILES_DIRS: {STATICFILES_DIRS}")

# Add this to check collected files after collectstatic

collected_files = os.path.join(STATIC_ROOT, 'images', 'favicon_io')
print("\nCHECKING COLLECTED FILES:")
if os.path.exists(collected_files):
    print(f"Files in {collected_files}:")
    print(os.listdir(collected_files))
else:
    print(f"Directory not found: {collected_files}")



LOGIN_REDIRECT_URL = '/account/'  # This should match your dashboard URL    