from .common import *
# development stuff here

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True
# Template Settings
TEMPLATE_DEBUG = False


INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.178.41',
    '192.168.105.1',
)

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'trendsetter',
        # The following settings are not used with sqlite3:
        'USER': 'vagrant',
        'PASSWORD': 'nopass',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'