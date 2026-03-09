import os

class Config:
    DEBUG = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://user:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
