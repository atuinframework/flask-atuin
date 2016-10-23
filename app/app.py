import os
from atuin.handler import app
app.jinja_loader.searchpath.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/templates')
