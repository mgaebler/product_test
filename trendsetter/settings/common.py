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
import sys
import markdown

APP_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(APP_DIR, '..')
sys.path.insert(0, APP_DIR)

# Component import
from .components.pipeline import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = (
    ('Marian Gaebler', 'marian.gaebler@intosite.de'),
)

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
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'

JINJA2_EXTENSIONS = (
    'pipeline.jinja2.ext.PipelineExtension',
)

MARKUP_FIELD_TYPES = (
    ('markdown', markdown.markdown),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

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
    # 'django_thumbor',
    'django_jinja',
    'django_jinja.contrib._humanize',
    'pipeline',
    # 'django_jinja.contrib._pipeline',
    'easy_thumbnails',
    'django_jinja.contrib._easy_thumbnails',
    'crispy_forms',
    # our apps
    'user_accounts', # the user profiles
    'faq',
    'forum',
    #'gallery',
    'product_test',
    'simple_bank',
    'simple_shop',
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

AUTH_USER_MODEL = 'user_accounts.UserAccount'

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

USE_X_FORWARDED_HOST = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '.static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.FileSystemFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/tmp/trendsetter/django_cache',
#     },
#     'staticfiles': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/tmp/trendsetter/django_cache_staticfiles',
#     },
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'local-memory'
    },
    'staticfiles': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'local-memory',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log', 'debug.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

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
