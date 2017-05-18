"""Provides functionality for querying data from a rein node"""

import requests

KNOWN_SERVERS = ['127.0.0.1:5000'] # 'rein1-sfo.reinproject.org:2016', 'rein2-ams.reinproject.org:2016'

def does_user_exist(delprivkey):
	"""Checks for a user's existence on all known servers based on his user id"""

	# Convert to msin
	msin = delprivkey
	for server in KNOWN_SERVERS:
		response = requests.get('http://{}/users/exists/{}'.format(server, msin)).text
		print(response)
		if response == 'True':
			return True

	return False
	