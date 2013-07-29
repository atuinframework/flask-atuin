# -.- coding: utf-8 -.-
#db utilities
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from sqlalchemy import event
from sqlalchemy.orm.attributes import NO_VALUE, NEVER_SET

import settings

def create_tables(db_handler, *tables):
	"""
		Creates all the tables from their models.
		Needs the db_handler as first parameter, and all the models thereafter
		Returns a tuple of models used	
	"""
	for t in tables:
		t.__table__.create(db_handler.engine, checkfirst=True)

	return tables


def drop_tables(db_handler, *tables):
	"""
		drop all the tables from their models.
		Needs the db_handler as first parameter, and all the models thereafter
		Returns a tuple of models used	
	"""
	for t in tables:
		t.__table__.drop(db_handler.engine, checkfirst=True)

	return tables


#Mokey patching to permit:
#	db.create_tables(Model1, Model2, ...)
#	db.drop_tables(Model1, Model2, ...)
db.create_tables = create_tables
db.drop_tables = drop_tables
