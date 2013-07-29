# Flask - Atuin

Atuin is Scalebox's Flask web application skeleton

## Package requirements (TODO: pip requirements file):

 - Flask (pip install flask)
 - flask-login (pip install flask-login)
 - SQLAlchemy (pip install sqlalchemy)
 - Flask-SQLAlchemy (pip install flask-sqlalchemy)
 - flask-cache (pip install flask-cache)
 - flask-babel (pip install flask-babel)
 - requests (pip install requests)

Install all:

    apt-get install python-dev
    pip install -U flask flask-login sqlalchemy flask-sqlalchemy flask-cache flask-babel requests

## Launch devserver

    ./dev.py

 or, for external use

    ./dev.py external

# Production Environment

## Installing uWSGI

    apt-get install python-dev
    apt-get install uwsgi-plugin-python uwsgi-plugin-http

## Production server uWSGI emperor

    sudo su -
	
uWSGI works in Emperor mode. So we only need to configure the workers (vassals).
 
 - create link in /etc/uwsgi/apps-available

        ln -s /home/project/prj/uwsgi.ini /etc/uwsgi/apps-available/project.ini

 - activate it
 
        ln -s /etc/uwsgi/apps-available/project.ini /etc/uwsgi/apps-enabled/project.ini

 - start the emperor
 
        service uwsgi start

## NGINX

Installation

    apt-get install nginx

 - create file _/etc/nginx/sites-available/project_ with following content

        upstream bt_app_server {
        	server 127.0.0.1:3032;
        }
        
        server {
        	listen 80;
        	server_name localhost;
        
        	location /static {
                alias /home/project/prj/static/;
        	}
        
        	location /static/bootstrap {
                alias /home/project/prj/static/bootstrap/;
        	expires 24h;
        	}
        
        	location / {
                try_files $uri @proxy_to_app;
        	}
        
        	location @proxy_to_app {
                uwsgi_pass bt_app_server;
                include uwsgi_params;
        	}
        }

 - activate it
 
        ln -s _/etc/nginx/sites-available/project_ _/etc/nginx/sites-enabled/project_


# Other tools

## App Python shell:

    ./shell.py

with `auth.models` preloaded

    ./shell.py auth

## DB reset:

	./initdb.py
 

