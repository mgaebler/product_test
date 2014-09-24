from .common import *
# development stuff here

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Template Settings
TEMPLATE_DEBUG = True
DEBUG_TOOLBAR = True

INTERNAL_IPS = (
    '*',
)

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '.media')