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
import raven
import sys

from logging.handlers import SysLogHandler

SITE_ID = 1

APP_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(APP_DIR, '..')
# add django_app to syspath
sys.path.insert(0, APP_DIR)

# Component import
from .components.pipeline import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher'
)

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
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',
)

# jinja 2 settings
# # http://niwibe.github.io/django-jinja/#_introduction
TEMPLATE_LOADERS = (
    'django_jinja.loaders.FileSystemLoader',
    'django_jinja.loaders.AppLoader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'
DEFAULT_FROM_EMAIL = 'info@trendsetter.eu'

JINJA2_EXTENSIONS = (
    'pipeline.jinja2.ext.PipelineExtension',
)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'grappelli',  # 3rd party
    'filebrowser',  # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'django_jinja',
    'django_jinja.contrib._humanize',
    'django_extensions',
    'django_nose',
    'pipeline',
    'manifesto',
    'easy_thumbnails',
    'django_jinja.contrib._easy_thumbnails',
    'core.django_jinja.contrib._bootstrapform',
    'core.django_jinja.contrib._common',
    'core.django_jinja.contrib._allauth',
    'raven.contrib.django.raven_compat',

    # our apps
    'core',
    'user_accounts',  # the user profiles
    'faq',
    'django_simple_forum',
    'gallery',
    'product_test',
    'senseo',
    'simple_bank',
    'simple_shop',
    'simple_comments',
    'static_pages',
    'raffles',
    'forms_builder.forms',
    'stickerz',
    'surveys',
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
    'static_pages.middleware.FlatpageFallbackMiddleware',
    'core.middleware.LogoutMiddleware',
)

ROOT_URLCONF = 'django_app.urls'

WSGI_APPLICATION = 'django_app.wsgi.production.application'

AUTH_USER_MODEL = 'user_accounts.UserAccount'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
SOCIALACCOUNT_QUERY_EMAIL = True

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

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
    # 'pipeline.finders.FileSystemFinder',
    # 'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

LOGIN_URL = "/my/login-form"

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
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'handlers': {
        'syslog': {
            'level': 'ERROR',
            'class': 'logging.handlers.SysLogHandler',
            # 'formatter': 'verbose',
            'facility': SysLogHandler.LOG_LOCAL2,
            'address': '/dev/log',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'product_test': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': True,
        },
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
#    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


#
# NOSE
#
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


#
# GRAPPELLI
#
GRAPPELLI_ADMIN_TITLE = 'Trendsetter Admin'


#
# SENTRY
#
RAVEN_CONFIG = {
    'dsn': 'https://d8b2c9f2b7284318a3226ddd230f86cc:9ccd57b28f974fdabf2aa8f1d072084b@app.getsentry.com/27588',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}