"""Provides functionality for the sign-in view"""

from kivy.lang import Builder

from functionality.Setting import Setting
from functionality.queries import does_user_exist

def import_identity(delprivkey, feedback_label):
	if not delprivkey:
		feedback_label.text = 'Please enter a key.'

	else:
		# Only set private key if it is associated with an identity on a known server
		if does_user_exist(delprivkey):
			Setting.make('delprivkey', delprivkey)
			# Switch to main screen

		else:
			feedback_label.text = 'The key you have entered is not associated with an identity.'

	# Check for key validity (is the key associated with an identity?)
	
	return True
