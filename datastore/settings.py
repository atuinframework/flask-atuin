# DB Configuration
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.dirname(__file__) + '/../sqlite_databases/main.db'
print "DB:", SQLALCHEMY_DATABASE_URI

