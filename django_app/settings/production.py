import yaml
from .common import *

ansible_vars = {}
with file(os.path.join(BASE_DIR, 'ansible', 'group_vars', 'production.yml')) as f:
    ansible_vars = yaml.load(f.read())

# production settings here
WSGI_APPLICATION = 'django_app.wsgi.production.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
THUMBNAIL_DEBUG = False

# Template Settings
TEMPLATE_DEBUG = False
DEBUG_TOOLBAR = False

# https://django-pipeline.readthedocs.org/en/latest/storages.html
STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineCachedStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail00.exor'
DEFAULT_FROM_EMAIL = 'staging@trendsetter.eu'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trendsetter2',
        'USER': 'trendsetter2',
        'PASSWORD': 'miejohrohm1iechedeeY4be9P',
        'HOST': 'intodb.exor',
        'PORT': '',
    }
}