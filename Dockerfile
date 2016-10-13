# vim:set ft=dockerfile:

# LOCAL DEVEL Dockerfile Test uWSGI

FROM scalebox/atuin-flask-webdev

MAINTAINER Paolo Casciello <paolo.casciello@scalebox.it>

RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    libcairo2 \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev

COPY ./requirements.txt /var/uwsgi/

WORKDIR /var/uwsgi

RUN pip install -r requirements.txt
