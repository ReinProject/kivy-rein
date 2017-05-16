"""Provides an interface for interaction with the sqlite database"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database(object):
    """Interface for interaction with the sqlite database"""

    def __init__(self, db_path='kivy-rein'):
        """Initializes the database file and create all tables"""

        self.engine = create_engine('sqlite:///{}.db'.format(db_path))

        from .Setting import BASE
        BASE.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()

    def close(self):
        """Closes the session"""

        return self.session.close()
