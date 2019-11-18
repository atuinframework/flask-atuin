# -*- coding: utf-8 -*-

# Configuration template file. Copy it to config.py
import os

# True to print all queries and autoreload
DEBUG = True

# change for each installation
SECRET_KEY = 'CHANGEME123123123'

# DATABASE URI override
SQLALCHEMY_DATABASE_URI = 'mysql://root:rootpwd@mariadb/atuin'

# site title
SITE_TITLE = "FLASK Atuin"

# multilanguage support
MULTILANGUAGE = False
MULTILANGUAGE_LANGS = ['en', ]

# considered only in production (DEBUG False)
#CACHE_CONFIG = {'CACHE_TYPE': 'memcached'}
CACHE_CONFIG = {'CACHE_TYPE': 'simple'}

APPCONFIG = {
    'customvar1': 'MyValue 1'
}