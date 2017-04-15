# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, g, redirect, url_for

from atuin.auth import current_user

bp = Blueprint('home', __name__)

@bp.route("/")
def index():
	return render_template("home/index.html")
