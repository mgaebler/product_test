# coding: utf8
"""
Django settings for trendsetter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')


# Component import
from .components.pipeline import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hvsz57&*mt(_p1$=#!%8eeo4jzl(v%k3wjsdl5dynt(b1*#&a2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Template Settings
TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

# jinja 2 settings
## http://niwibe.github.io/django-jinja/#_introduction
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django_jinja.loaders.AppLoader',
        'django_jinja.loaders.FileSystemLoader',
    )),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

JINJA2_EXTENSIONS = (
    'pipeline.jinja2.ext.PipelineExtension',
)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli', # 3rd party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'django_thumbor',
    'django_jinja',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'trendsetter.urls'

WSGI_APPLICATION = 'trendsetter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '.static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

## THUMBOR SETTINGS
# The host serving the thumbor resized images
THUMBOR_SERVER = 'http://localhost:8888'

# The prefix for the host serving the original images
# This must be a resolvable address to allow thumbor to reach the images
THUMBOR_MEDIA_URL = 'http://localhost:8000/media'

# The same security key used in the thumbor service to
# match the URL construction
THUMBOR_SECURITY_KEY = 'MY_SECURE_KEY'

# Default arguments passed to the `generate_url` helper or
# the `thumbor_url` templatetag
THUMBOR_ARGUMENTS = {}