from flask.ext import login

login_manager = login.LoginManager()
login_required = login.login_required
current_user = login.current_user