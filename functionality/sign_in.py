"""Provides functionality for the sign-in view"""

from kivy.lang import Builder

from functionality.Setting import Setting
from functionality.queries import does_user_exist

def import_identity(delprivkey, feedback_label, screen_manager):
	if not delprivkey or len(delprivkey) < 40:
		feedback_label.text = 'Please enter a key.'

	else:
		# Only set private key if it is associated with an identity on a known server
		if does_user_exist(delprivkey):
			Setting.make('delprivkey', delprivkey)
			screen_manager.current = 'MainScreen'

		else:
			feedback_label.text = 'The key you have entered is not ' \
				'associated with an identity or invalid.'
	
	return True
