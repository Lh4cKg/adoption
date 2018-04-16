# _*_ coding: utf-8 _*_

"""
Created on Apr 16, 2018

@author: Lasha Gogua
"""

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'adoption',  # Or path to database file if using sqlite3.
        'USER': 'zarko',  # Not used with sqlite3.                 # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
        'PASSWORD': 'password'
        # 'OPTIONS': {""}                      # Set to empty string for default. Not used with sqlite3.
    }
}

