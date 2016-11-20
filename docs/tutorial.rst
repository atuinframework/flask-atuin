Flask-Atuin Mega Tutorial
=========================

This is a step-by-step guide on working with Flask-Atuin.

We will create a basic Twitter clone.

Prerequisites
-------------

* Working Mercurial version control system (Git is planned in the future)
* Working Docker with Docker-Compose support

Start a new project
-------------------

Using Mercurial
***************

You can clone the latest Flask-Atuin version and then copy the package::

	$ hg clone https://xcash@bitbucket.org/scalebox/flask-atuin
	$ cd flask-atuin
	
**only until release** move on v2 branch ::
	
	$ hg up -C xcash-v2
	
Create an unversioned project directory::
  
	$ hg archive <destination-folder like ../atuitter>
	
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
	├── babel.cfg           (<-- atuin internal for i18n)
	├── docker-compose.docs.yml (<-- docker compose file for docs)
	├── docker-compose.yml      (<-- main docker-compose file)
	├── Dockerfile           (<-- containers definitions)
	├── Dockerfile.docs      ( ... )
	├── Dockerfile.mariadb   ( ... )
	├── Dockerfile.tools     ( ... )
	├── docs        (<-- this docs source)
	├── mariadb.cnf (<-- mariadb configuration)
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

Once everything started let's try our new website by connecting to http://localhost:5000

You'll se an Hello World screen followed by a login form. It worked!

Our first template
------------------

...

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



