import requests
import json

from settings import DEBUG, SITE_TITLE
from logs.models import Log

MANDRILL_BASE_URI = 'https://mandrillapp.com/api/1.0/'
JSON_MAIL_TMPL  = {
		'key': 'YOUR SECRET KEY',
		'message': {
				'from_email': "info@example.com",
				'from_name': SITE_TITLE ,
				'track_clicks': False,
				'subject': '',
				'html': "",
				'tags': [ ],
		}
}

def send_mail(subject, message, tolist, cclist=[], bcclist=[], tags=[]):
	req_d = JSON_MAIL_TMPL.copy()
	req_d['message']["subject"] = subject
	req_d['message']["html"] = message
	req_d['message']['to'] = tolist
	req_d['message']['bcc'] = bcclist
	req_d['message']['tags'] += tags
	
	Log.log_event('MAIL', 'To: {} - Subj: {}'.format(','.join([e['email'] for e in tolist]), subject))
	if DEBUG:
		return True
	else:
		r = requests.post(MANDRILL_BASE_URI+'messages/send.json', data=json.dumps(req_d))
		return (r.status_code == 200)
