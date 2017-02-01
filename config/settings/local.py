# -*- coding: utf-8 -*-

"""
Local settings

- Run in Debug mode
- Use console backend (mailhog) for emails
- Add django-extensions and debug_toolbar app
"""

from __future__ import absolute_import, unicode_literals

from .common import *

# APP CONFIGURATION
# ******************************************************************************

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='qln(=3!pf+e$1k6s6zwjq(&3gsf73xjl=fu&40p_eqy=js%sk1')

# Django-extensions: https://github.com/django-extensions/django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions',)

# Debug Toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['file', 'console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
            'datefmt': '%d-%m-%Y %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/pdepou.log',
            'maxBytes': 1024 * 1024,  # 1 MB
            'backupCount': 3,
            'encoding': 'utf8',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'blog': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
            'propagate': False,
        }
    },
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
