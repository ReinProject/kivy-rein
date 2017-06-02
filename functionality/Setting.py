"""Provides functionality for saving and reading settings from the local db"""

from functionality.Database import DATABASE

class Setting():
	@staticmethod
	def make(setting_name, setting_value):
		"""Inserts a setting into the database or updates it if the setting has been set"""

		if Setting.read(setting_name):
			t = (setting_value,setting_name,)
			DATABASE.cursor.execute('''UPDATE settings
				SET setting_value = ?
				WHERE setting_name = ?''', t)

		else:
			t = (setting_name, setting_value,)
			DATABASE.cursor.execute('''INSERT INTO settings
				(setting_name, setting_value)
				VALUES(?, ?)''', t)

		DATABASE.connection.commit()

	@staticmethod
	def read(setting_name):
		"""Returns a setting's value or None if that setting has not been set"""

		t = (setting_name,)
		DATABASE.cursor.execute('''SELECT setting_value 
			FROM settings 
			WHERE setting_name = ?''', t)
		result = DATABASE.cursor.fetchone()
		if result:
			return result[0]

		return None
