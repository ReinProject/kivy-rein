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
		if response == 'True':
			return True

	return False

def get_active_jobs(delprivkey):
	"""Gets all active jobs a user is involved in"""

	active_jobs = []
	previous_job_names = []
	delegate_public_key = pybitcointools.privtopub(delprivkey)
	for server in KNOWN_SERVERS:
		response = requests.get('http://{}/users/by_pubkey/{}/jobs/active'.format(server, delegate_public_key)).json()
		if 'message' not in response:
			for job in response:
				# Avoid adding two copies of the same job from different servers
				if job['name'] not in previous_job_names:
					active_jobs.append(job)
					previous_job_names.append(job['name'])

	return active_jobs
