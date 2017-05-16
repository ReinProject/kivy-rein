"""Provides functionality for the sign-in view"""

from functionality.Setting import Setting

def import_identity(delprivkey, feedback_label):
	if not delprivkey:
		feedback_label.text = 'Please enter a key.'

	else:
		Setting.make('delprivkey', delprivkey)

	# Check for key validity (is the key associated with an identity?)
	
	return True
