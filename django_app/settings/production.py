import yaml
from .common import *


ENVIRONMENT = 'production'

# production settings here
WSGI_APPLICATION = 'django_app.wsgi.production.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
THUMBNAIL_DEBUG = False

# Template Settings
TEMPLATE_DEBUG = False
DEBUG_TOOLBAR = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail00.exor'
DEFAULT_FROM_EMAIL = 'info@product-test.eu'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'product-test2',
        'USER': 'product-test2',
        'PASSWORD': 'miejohrohm1iechedeeY4be9P',
        'HOST': 'intodb.exor',
        'PORT': '',
    }
}

