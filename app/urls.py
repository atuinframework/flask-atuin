#public site imports
# import section.views / admin
import home.views

#admin & auth
import atuin.auth.views, atuin.auth.admin
# import atuin.admin.views
import atuin.js_translations.views


mounts = [
	('/', home.views),
	
	('/auth', atuin.auth.views),
	
	# ('/admin', atuin.admin.views),
	
	# ATUIN
	('/admin/auth', atuin.auth.admin),
	('/', atuin.js_translations.views),


]
