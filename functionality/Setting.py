"""Provides the setting model and functionality for saving and reading settings"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from functionality.Database import Database

BASE = declarative_base()
DATABASE = Database()

class Setting(BASE):
    """Provides the setting model and functionality for saving and reading settings"""

    __tablename__ = 'settings'
    setting_id = Column(Integer, primary_key=True)
    setting_name = Column(String)
    setting_value = Column(String)

    @staticmethod
    def make(setting_name, setting_value):
        """Adds a new setting to the database or updates an existing setting"""

        setting_in_db = DATABASE.session.query(Setting).filter(Setting.setting_name == setting_name).first()
        if not setting_in_db:
            setting = Setting()
            setting.setting_name = setting_name
            setting.setting_value = setting_value
            DATABASE.session.add(setting)

        else:
            setting_in_db.setting_value = setting_value

        DATABASE.session.commit()

    @staticmethod
    def read(setting_name):
        """Reads a setting's value from the database"""

        setting_in_db = DATABASE.session.query(Setting).filter(Setting.setting_name == setting_name).first()
        if not setting_in_db:
            return None

        return setting_in_db.setting_value

    @staticmethod
    def delete(setting_name):
        """Removes a setting from the database"""

        setting_in_db = DATABASE.session.query(Setting).filter(Setting.setting_name == setting_name).delete()
        DATABASE.session.commit()
