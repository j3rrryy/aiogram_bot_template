import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, unique=True, nullable=False, primary_key=True)


class YourModel(Base):
    __tablename__ = '<table_name_>'
