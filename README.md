# Flask - Atuin

[Atuin Web Framework] is a Flask powered web application framework built by 
[SCALEBOX s.r.l.] an Italian IT company that provides a complete web application
 skeleton.

Goal of Atuin is maintaining the same developing philosophy when dealing with 
*traditional* relational database stack or when targeting Google App Engine 
environment and using the Google Datastore.

Atuin includes some useful Flask extensions for common tasks such as 
authentication, localization, caching.

## Develop using Docker

## Launch development environment

...

## Custom requirements

...

# Running in production

...

# Other tools

## App Python shell:

    ...

with `auth.models` preloaded

    ... auth

## DB Manage and migrations

FlaskAtuin uses Flask-migrate

### First db init (used only when project is **started**)

    ... ./initdb.py db init

### Upgrade to latest migrations

    ... ./initdb.py db upgrade

### To generate new migration

    ... ./initdb.py db migrate -m "description"

*check the files* and then **apply**

    ... ./initdb.py db upgrade

# Translations

...

[Atuin Web Framework]: https://github.com/atuinframework
[SCALEBOX s.r.l.]: https://www.scalebox.it/
