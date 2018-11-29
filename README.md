# Flask Atuin - A web application skeleton 

[Atuin Web Framework] is a Flask powered web framework built by [SCALEBOX s.r.l.], an Italian IT Agency, that provides a complete web application skeleton to kick-start a new project.

Goal of Atuin is maintaining the same developing philosophy when dealing with *traditional* relational database stack and targeting [Google App Engine] using [Cloud Datastore].
Usually you only need to change the data codebase and nothing else when porting between the two.

Atuin includes some useful Flask extensions for common tasks such as authentication, localization, caching. Look at the repository for more details. :)

Atuin free to use for all.


## Features

- [Flask] as the base **WSGI** Python framework
- [SQLAlchemy] as **ORM**
- [Babel] for i18n (translations, internationalization)
- **Full authentication system** out of the box
- Completely **Dockerized** environment (you don't need to install libraries or other things, just a working Docker)
- Well defined project structure to handle code maintainability and project growth
- **Static files automatic optimization** (CSS, JS, images, etc..) through the [Atuin tools] container
- **Easy update**. Just replace ``app/atuin`` package



## Quick start

```bash
git clone git@github.com:atuinframework/flask-atuin.git

cd flask-atuin

docker-compose up

```

Checkout the [documentation] to get started!


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
[Google App Engine]: https://cloud.google.com/appengine/
[Datastore]: https://cloud.google.com/datastore/
[Flask]: http://flask.pocoo.org/
[SQLAlchemy]: https://www.sqlalchemy.org/
[Atuin tools]: https://github.com/atuinframework/atuin-tools
[Babel]: http://babel.pocoo.org/en/latest/
[documentation]: https://flask-atuin.readthedocs.io