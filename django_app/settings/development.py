import yaml
from .common import *
# development stuff here

ansible_vars = {}
with file(os.path.join(BASE_DIR, 'ansible', 'group_vars', 'vagrant.yml')) as f:
    ansible_vars = yaml.load(f.read())

ENVIRONMENT = 'development'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True
# Template Settings
TEMPLATE_DEBUG = False

WSGI_APPLICATION = 'django_app.wsgi.development.application'

# ok, this is a bit weird. PIPELINE_ENABLED = True means, if debug is true pipeline is off.
# So to re-enable it just comment the next line.
# PIPELINE_ENABLED = True

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.178.41',
    '192.168.105.1',
)

INSTALLED_APPS += (
    'debug_toolbar',
    # 'debug_toolbar.apps.DebugToolbarConfig',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'