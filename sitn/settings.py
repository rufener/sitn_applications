"""
Django settings for sitn project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY') 

# SECURITY WARNING: don't run with debug turned on in production!
DEVELOPMENT_MODE = False

if 'DEVELOPMENT_MODE' in os.environ and os.environ['DEVELOPMENT_MODE'] == "True":
    DEVELOPMENT_MODE = True

DEBUG = DEVELOPMENT_MODE 

ALLOWED_HOSTS = os.environ["ALLOWED_HOST"].split(",")

# Application definition

INSTALLED_APPS = [
    'cats.apps.CatsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.RemoteUserBackend',
]

ROOT_URLCONF = 'sitn.urls'

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

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'OPTIONS': {
            'options': '-c search_path=' + os.environ["PGSCHEMA"] + ',public'
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-ch'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

FORCE_SCRIPT_NAME = os.environ.get('ROOTURL', '')

STATIC_URL = FORCE_SCRIPT_NAME + '/assets/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

WHITENOISE_STATIC_PREFIX = "/assets/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEVELOPMENT_MODE is True:
    GDAL_PATH = os.environ["GDAL_PATH"]
    GDAL_LIBRARY_PATH = os.environ["GDAL_LIBRARY_PATH"]
    os.environ['GDAL_DATA'] = GDAL_PATH + "gdal-data"
    os.environ['PROJ_LIB'] = GDAL_PATH + "projlib"
    GDAL_LIBRARY_PATH = os.environ["GDAL_LIBRARY_PATH"]
    GEOS_LIBRARY_PATH = os.environ["GEOS_LIBRARY_PATH"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {module} {filename} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOGGING_LEVEL', 'ERROR'),
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('LOGGING_LEVEL', 'ERROR'),
            'propagate': False,
        },
    },
}
