import yaml
from .common import *

ansible_vars = {}
with file(os.path.join(BASE_DIR, 'ansible', 'group_vars', 'staging.yml')) as f:
    ansible_vars = yaml.load(f.read())

ENVIRONMENT = 'staging'

WSGI_APPLICATION = 'django_app.wsgi.staging.application'

# SECURITY WARNING: don't run with debug turned on in production
DEBUG = True
THUMBNAIL_DEBUG = True
# Template Settings
TEMPLATE_DEBUG = False

# ok, this is a bit weird. PIPELINE_ENABLED = True means, if debug is true pipeline is off.
# So to re-enable it just comment the next line.
PIPELINE_ENABLED = True

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
DEFAULT_FROM_EMAIL = 'staging@product-test.eu'

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
            'level': 'DEBUG',
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
        'user_account.view': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },

}
