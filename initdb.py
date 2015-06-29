#!/usr/bin/env python
# - coding: utf-8 -
import sys
import datetime
import random
import csv

from handler import app
from datastore import db

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


from auth.models import *
from logs.models import *



@manager.command
def create_admin():
	print "Creating admin..."
	
	u = User(usertype="staff", username="admin", name="Admin", role="ADMIN")
	u.set_password('admin')
	db.session.add(u)

	db.session.commit()


@manager.command
def create_demo_users():
	print "Deleting demo users..."
	
	db.session.commit()

@manager.command
def update_policies():
	print "Updating policies..."
	
	UserPolicy.query.delete()
	
	db.session.add(UserPolicy(role='AGENT', functions=','.join([
		
															])))
	
	db.session.add(UserPolicy(role='USER', functions=','.join([
		
															])))
	
	db.session.commit()



@manager.command
def create_demo_data():
	print "Deleting demo data..."
	
	
	print "Creating demo data..."

	
	db.session.commit()


if __name__ == '__main__':
	manager.run()
	

	
