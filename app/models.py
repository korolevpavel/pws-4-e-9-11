from sqlalchemy import *
from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'

    _id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    email = Column(String, primary_key=True)
    password = Column(String)
    authenticated = Column(Boolean, default=False)

    def get_id(self):
        return self._id

    def is_authenticated(self):
        return self.authenticated


class Event(Base):
    __tablename__ = 'events'

    _id = Column(Integer, primary_key=True)
    date_start = Column(DateTime, unique=False, nullable=False)
    date_end = Column(DateTime, unique=False, nullable=False)
    author = Column(Integer, ForeignKey('users._id'), nullable=False)
    subject = Column(String(80), unique=False, nullable=False)
    description = Column(String(300), unique=False, nullable=True)
