# -*- coding: utf-8 -*-

"""
Production Configurations

- Use Sendgrid to send emails
"""

from __future__ import absolute_import, unicode_literals

from .common import *

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
SECRET_KEY = env('DJANGO_SECRET_KEY')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# Raises ImproperlyConfigured exception if database defaults not in os.environ
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='127.0.0.1'),
        'PORT': env('DB_PORT', default='5432'),
        'CONN_MAX_AGE': env('DB_CONN_MAX_AGE', default=300)
    }
}

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default=[])

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='sendgrid_username')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='sendgrid_password')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

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
