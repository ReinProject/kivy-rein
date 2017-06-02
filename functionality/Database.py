"""Provides an interface for interaction with the sqlite database"""

import os
from sqlite3 import connect

class Database(object):
    """Interface for interaction with the sqlite database"""

    def __init__(self, db_path='kivy-rein'):
        """Initializes the database file and create all tables"""

        existing_database = os.path.exists('{}.db'.format(db_path))
        self.connection = connect('{}.db'.format(db_path))
        self.cursor = self.connection.cursor()
        if not existing_database:
            create_settings_table = '''CREATE TABLE settings
            (setting_id INTEGER PRIMARY KEY ASC,
            setting_name TEXT,
            setting_value TEXT)'''
            self.cursor.execute(create_settings_table)

    def close(self):
        """Closes the connection"""

        return self.connection.close()

DATABASE = Database()
