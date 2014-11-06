import yaml
from .common import *

ansible_vars = {}
with file(os.path.join(BASE_DIR, 'ansible', 'group_vars', 'staging.yml')) as f:
    ansible_vars = yaml.load(f.read())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True
# Template Settings
TEMPLATE_DEBUG = False


INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail00.exor'
DEFAULT_FROM_EMAIL = 'staging@trendsetter.eu'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ansible_vars['app']['id'],
        'USER': ansible_vars['app']['id'],
        'PASSWORD': ansible_vars['app']['id'],
        'HOST': 'localhost',
        'PORT': '',
    }
}