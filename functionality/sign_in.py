"""Provides functionality for the sign-in view"""

from functionality.Setting import Setting
from functionality.queries import does_user_exist
from functionality.main_screen import set_user_job_data

def import_identity(delprivkey, feedback_label, screen_manager):
	if not delprivkey or len(delprivkey) < 40:
		feedback_label.text = 'Please enter a key.'

	else:
		# Only set private key if it is associated with an identity on a known server
		if does_user_exist(delprivkey):
			Setting.make('delprivkey', delprivkey)
			screen_manager.current = 'MainScreen'
			set_user_job_data(screen_manager)

		else:
			feedback_label.text = 'The key you have entered is not ' \
				'associated with an identity or invalid.'
	
	return True
