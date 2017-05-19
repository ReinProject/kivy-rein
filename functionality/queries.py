"""Provides functionality for querying data from a rein node"""

import requests
import pybitcointools

KNOWN_SERVERS = ['127.0.0.1:5000'] # 'rein1-sfo.reinproject.org:2016', 'rein2-ams.reinproject.org:2016'

def does_user_exist(delprivkey):
	"""Checks for a user's existence on all known servers based on his private key"""

	try:
		delegate_public_key = pybitcointools.privtopub(delprivkey)
		delegate_address = pybitcointools.pubtoaddr(delegate_public_key)

	except AssertionError:
		return False
		
	for server in KNOWN_SERVERS:
		response = requests.get('http://{}/users/exists/{}'.format(server, delegate_address)).text
		print(response)
		if response == 'True':
			return True

	return False

def get_active_jobs(delprivkey):
	"""Gets all active jobs a user is involved in"""

	return ['Job {}'.format(i) for i in range(100)]
