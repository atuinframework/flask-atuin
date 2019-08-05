# vim:set ft=dockerfile:

# LOCAL DEVELOPMENT Dockerfile

FROM atuinframework/flask-atuin-devenv:v3-py2

LABEL maintainer="Paolo Casciello <paolo.casciello@scalebox.it>"

COPY ./requirements.txt /var/wsgi/

WORKDIR /var/wsgi

RUN pip install -r requirements.txt

# IS POSSIBLE TO OVERRIDE STARTING SCRIPT
# COPY ./start.sh /var/wsgi-commands
