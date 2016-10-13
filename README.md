# Flask - Atuin

Atuin is Scalebox's Flask web application skeleton

## Develop using Docker

## Launch development environment

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