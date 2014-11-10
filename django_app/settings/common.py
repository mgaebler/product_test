# coding: utf-8
"""
Django settings for django_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import markdown

from logging.handlers import SysLogHandler


APP_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(APP_DIR, '..')
sys.path.insert(0, APP_DIR)

# Component import
from .components.pipeline import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = (
    ('Intosite Developers', 'devs@intosite.de'),
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
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
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
DEFAULT_FROM_EMAIL = 'info@trendsetter.de'


JINJA2_EXTENSIONS = (
    'pipeline.jinja2.ext.PipelineExtension',
)

MARKUP_FIELD_TYPES = (
    ('markdown', markdown.markdown),
)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'grappelli',  # 3rd party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'authtools',
    'social.apps.django_app.default',
    'django_jinja',
    'django_jinja.contrib._humanize',
    'django_extensions',
    'pipeline',
    'manifesto',
    # 'django_jinja.contrib._pipeline',
    'easy_thumbnails',
    'django_jinja.contrib._easy_thumbnails',
    'core.django_jinja.contrib._bootstrapform',
    # 'bootstrapform',
    'django_nose',

    # our apps
    'core',
    'user_accounts',  # the user profiles
    'faq',
    'django_simple_forum',
    'gallery',
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

ROOT_URLCONF = 'django_app.urls'

WSGI_APPLICATION = 'django_app.wsgi.production.application'

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

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

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
# 'default': {
# 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
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
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            # 'formatter': 'verbose',
            'facility': SysLogHandler.LOG_LOCAL2,
            'address': '/dev/log',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django_jinja.builtins.global_context': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': True,
        },

    },

}


AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    # '--logging-level=INFO',
    # '--verbosity=3',
    '--with-spec',
    '--spec-color',
    # '--with-progressive',
    # '--logging-clear-handlers',
    # '--with-coverage',
    # '--no-skip'
]

# grappelli
GRAPPELLI_ADMIN_TITLE = 'Trendsetter Admin'