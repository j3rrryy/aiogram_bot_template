from sqlalchemy import Column, Integer, VARCHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class YourModel(Base):
    __tablename__ = '<table_name_>'
