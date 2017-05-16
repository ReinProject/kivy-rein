from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

BASE = declarative_base()

class Setting(BASE):
	__tablename__ = 'settings'
	setting_id = Column(Integer, primary_key=True)
	setting_name = Column(String)
	setting_value = Column(String)

	@staticmethod
	def make(database, setting_name, setting_value):
		setting_in_db = database.session.query(Setting).filter(Setting.setting_name == setting_name).first()
		if not setting_in_db:
			setting = Setting()
			setting.setting_name = setting_name
			setting.setting_value = setting_value
			database.session.add(setting)

		else:
			setting_in_db.setting_value = setting_value

		database.session.commit()

	@staticmethod
	def read(database, setting_name):
		setting_in_db = database.session.query(Setting).filter(Setting.setting_name == setting_name).first()
		if not setting_in_db:
			return None

		return setting_in_db.setting_value
