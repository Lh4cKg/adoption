# _*_ coding: utf-8 _*_

"""
Created on Apr 16, 2018

@author: Lasha Gogua
"""

from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

TIME_ZONE = 'Asia/Tbilisi'
