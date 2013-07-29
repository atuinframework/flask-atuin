#!/usr/bin/env python
# - coding: utf-8 -
import sys
import datetime

from handler import app
from datastore import db

from auth.models import *

if __name__ == '__main__':
	
	db.drop_all(app=app)
	db.create_all(app=app)
	
	app.test_request_context().push()
	
	u = User(usertype="staff", username="admin", name="Admin", role="ADMIN")
	u.set_password('admin')
	db.session.add(u)
	db.session.commit()

	
