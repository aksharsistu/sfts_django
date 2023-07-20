"""
Backend application for Shopfloor Traceability system.
Notes:
    1. Default apps have been removed including default auth app which has been replaced with a custom one
    2. Some security related middleWare has been removed for development purposes and can be configured at deployment
    3. Deployment of previous versions has been through Gunicorn and Nginx proxy while apache2 served the frontend
    4. django-cors-headers was installed through pip to allow requests from all users by setting CORS_ORIGIN_ALLOW_ALL=True
    5. Current database is set to sqlite3, can be configured to run with MySQL as used in the server
    6. Some files not critical for functioning of the apps have been removed from their directories
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-24e00s=ovz7rzh=8(g91($e#s_1p0s@m5kjv6r+g4&2@k7@%tx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'auth',
    'stage',
    'data',
    'process'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sfts.urls'


WSGI_APPLICATION = 'sfts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
