import os

from .base import *
from django.utils.translation import ugettext_lazy as _

DEBUG = True

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=django'
        },
        'NAME': 'gym_dev',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

STATIC_ROOT = '/var/www/gym-app/static/'

STATIC_URL = '/static/'