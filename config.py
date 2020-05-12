import os

DATABASE_URL = 'postgresql://postgres:admin@localhost:5432/events_bd'


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', DATABASE_URL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "app.py"
    # FLASK_DEBUG = True
    # FLASK_ENV = 'development'
    SECRET_KEY = os.getenv('SECRET_KEY', 'yoursecretkey12345')
