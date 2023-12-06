"""
Django settings for omniverse_drf project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta # for the simple_jwt dict

from dotenv import dotenv_values
from pathlib import Path
from utils.hashify import Hashify
from utils.marvel_api_handler import MarvelAPI
from time import time

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
ENVDB_PATH = BASE_DIR / ".env.db"
ENVMARVELAPI_PATH = BASE_DIR / ".env.marvelapi"

# base configurations.
CONFIG = dotenv_values(ENV_PATH)
SECRET_KEY = CONFIG["SECRET_KEY"]

# database configurations.
DBCONFIG = dotenv_values(ENVDB_PATH)

# Marvel API configurations
# All calls to the Marvel Comics API must pass your public key via an “apikey”
# parameter. Client-side and server-side applications have slightly different
# authentication rules in order to access the API. Please read below for the
# appropriate method for your application.
# REF: https://developer.marvel.com/documentation/authorization
# REF2: https://developer.marvel.com/docs
MARVELCONFIG = dotenv_values(ENVMARVELAPI_PATH)
MARVEL_API_KEY = MARVELCONFIG["PUBLIC_KEY"]
MARVEL_PVT_KEY = MARVELCONFIG["PRIVATE_KEY"]
MARVEL_API_ENDPOINT = MARVELCONFIG["ENDPOINT_URL"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "apps.omni_catalog.apps.OmniCatalogConfig",
    "apps.omni_market.apps.OmniMarketConfig",
    "apps.user_auth.apps.UserAuthConfig",
    "apps.user_collection.apps.UserCollectionConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", # added 2023-12-04 @ 1:37 PM EST
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "omniverse_drf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "omniverse_drf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": DBCONFIG['DB_ENGN'], # added: 2023-12-04 @ 10:00 AM EST
        "NAME": BASE_DIR / DBCONFIG['DB_FILE'], # added: 2023-12-04 @ 9:59 AM EST
        "USER": DBCONFIG['DB_USER'], # added: 2023-12-04 @ 9:54 AM EST
        "PASSWORD": DBCONFIG['DB_PASS'], # added: 2023-12-04 @ 9:54 AM EST
        "HOST": DBCONFIG['DB_HOST'], # added: 2023-12-04 @ 9:55 AM EST
        "PORT": DBCONFIG['DB_PORT'] # added: 2023-12-04 @ 9:55 AM EST
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# django-simplejwt settings.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
}

# REST framework authentication, etc.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
