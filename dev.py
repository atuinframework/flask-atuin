#!/usr/bin/env python
import sys

from handler import app

if __name__ == '__main__':
	print app.url_map
	if 'external' in sys.argv[1:]:
		app.run(host='0.0.0.0')
	else:
		app.run()
