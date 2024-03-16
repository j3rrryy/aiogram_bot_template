from sqlalchemy import Column, Integer, VARCHAR, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)


class YourModel(Base):
    __tablename__ = '<table_name_>'
