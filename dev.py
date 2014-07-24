#!/usr/bin/env python
import sys

from flask.ext.script import Manager

from handler import app

manager = Manager(app)


@manager.command
def run():
	print app.url_map
	app.run()

@manager.command
def runserver():
	run()

@manager.command
def external():
	app.run(host='0.0.0.0')
	

if __name__ == '__main__':
	manager.run()