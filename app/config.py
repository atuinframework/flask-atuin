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

# whether to use newrelic (autodiscovery mode)
NEWRELIC = False
NEWRELIC_CONFIG = "newrelic.ini"

# whether to use sentry
SENTRY_DSN = False

# S3 Auth Keys and bucket
S3_ACCESS_KEY_ID = ""
S3_SECRET_ACCESS_KEY = ""
S3_REGION_NAME = ""
S3_BUCKET_NAME = ""

