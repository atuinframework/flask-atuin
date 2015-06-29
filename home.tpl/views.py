import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, g, redirect, url_for

from auth import current_user


bp = Blueprint('home', __name__)

@bp.route("/")
def index():
	if current_user.is_authenticated():
		return redirect(url_for('admin.index'))
	
	return render_template("home/index.html")


