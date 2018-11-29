Flask-Atuin Mega Tutorial
=========================

This is a step-by-step guide on working with Flask-Atuin.

We will create a basic Twitter clone.

Prerequisites
-------------

* Working git version control system
* Working Docker with Docker-Compose support

Start a new project
-------------------

Using Git
*********

You can clone the latest Flask-Atuin version and then copy the package::

	$ git clone git@github.com:atuinframework/flask-atuin.git
	$ cd flask-atuin
	
**Move to latest release**::

	$ git checkout tags/<release_name>

Look for the latest release here: `flask-atuin/releases`_

Remove the `.git` directory, so to start with your new project::
  
	$ rm -rf .git
	
Using an archived package
*************************

Or extract a repository package ::

    $ tar xzf flask-atuin.tgz
    $ mv flask-atuin atuitter

*In Windows you must know how to do that commands.*

Project Structure
-----------------

The ``flask-atuin`` directory tree is structured for a basic Hello World example. You can use
this as a starting point, a skeleton for your project.

For our purposes we will copy this structure in our own project called *Atuitter*. :)

 In a future release there will probably be a script to initialize a new project.
 Until then... be patient :P

Following is an annotated view of the Hello World tree::

	.
	├── app                 (<-- app directory)
	│   ├── app.py          (<-- app WSGI entrypoint)
	│   ├── atuin           (<-- Atuin package)		
	│   ├── config.py       (<-- app config)
	│   ├── home            (<-- app section)
	│   ├── languages.py    (<-- available languages)
	│   ├── migrations      (<-- database migration directory)
	│   ├── static          (<-- app static files)
	│   ├── templates       (<-- app templates)
	│   ├── urls.py         (<-- url mounts (aka routing))
	│   └── version.py      (<-- current app version)
	├── config              (<-- config directory)
	│   ├── babel.cfg       (<-- atuin internal for i18n)
	│   └── mariadb.cnf     (<-- mariadb configuration)
	├── docker-compose.docs.yml (<-- docker compose file for docs)
	├── docker-compose.yml      (<-- main docker-compose file)
	├── Dockerfile           (<-- containers definitions)
	├── Dockerfile.docs      ( ... )
	├── Dockerfile.mariadb   ( ... )
	├── Dockerfile.tools     ( ... )
	├── docs        (<-- this docs source)
	├── README.md   (<-- guess it)
	├── requirements.txt     (<-- custom pip requirements)
	└── start.sh    (<-- this will be removed on release)


Basic configuration
-------------------

Let's start by configuring our amazing app!

config.py
*********

Change the ``SECRET_KEY`` and ``SITE_TITLE`` for now. ::

	[...]
	
	# change for each installation
	SECRET_KEY = 'MYSecret$ecret$Atuitter123@_'
	
	# site title
	SITE_TITLE = "Atuitter"
	
	[...]

``SECRET_KEY`` is the crypto key used to store cryptographically secure cookies on the client.
This value must be kept secret or someone could create malicious code to tamper your cookies.

``SITE_TITLE`` is the... you guessed it! ;)

Start the development environment
---------------------------------

Now it's time to test if all is working! ::

	$ docker-compose up
	
The first execution could be slow as it rebuilds the containers image and downloads the missing ones.

Once everything is started let's try our new website by connecting to http://localhost:5000

You'll se an Hello World screen followed by a login form. It worked!

Our first template
------------------

In Atuin there are two types of templates: the Atuin's builtin and your custom app templates.

Let's check if all is working by modifying our homepage template.

templates/home/index.html
*************************

Change the titles ::

	{% extends 'atuin/base.html' %}
	
	{% block content %}
	
	<div class="row" style="margin-top:20%">
		<div class="col-md-4 col-md-offset-4">
			<h3>{% trans %}This is Atuitter{% endtrans %}</h3>
			<div class="panel panel-default">
				<div class="panel-heading text-center">
					<h4 class="panel-title">Atuin's microblogging</h4>
				</div>
				<div class="panel-body">
					{% include 'atuin/auth/loginform.html' %}
				</div>
				<div class="panel-footer">
					<button class="btn btn-block btn-primary btnLogin" autocomplete="off">Login</button>
				</div>
			</div>
		</div>
	</div>
	
	{% endblock %}

Reload and we will see our new titles in the login form.

Our template extends Atuin's built in `atuin/base.html` (which is `atuin/templates/atuin/base.html`).
It defines the main page layout including Bootstrap, JQuery and Atuin's generated javascript files.

We need a database
------------------

...

Initialize database tables
--------------------------

...

Our first login
---------------

...

Our first Entity
----------------

...

Our first database migration
----------------------------

...

Time for some Javascript
------------------------

...

Add some styles!
----------------

...

Let's grow with a new section
-----------------------------

...

What about backend?
-------------------

...



.. _flask-atuin/releases: https://github.com/atuinframework/flask-atuin/releases