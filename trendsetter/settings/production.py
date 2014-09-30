from .common import *

# production settings here

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
THUMBNAIL_DEBUG = False
# Template Settings
TEMPLATE_DEBUG = False
DEBUG_TOOLBAR = False

# https://django-pipeline.readthedocs.org/en/latest/storages.html
STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineCachedStorage'