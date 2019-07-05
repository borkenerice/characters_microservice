import os

DEBUG = True
TESTING = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

POSTGRES_DEFAULT_USER = 'postgresql'
POSTGRES_USER = 'characters_micro'
POSTGRES_PASSWORD = 'characters_micro'
POSTGRES_DB = 'characters_micro-db'
SQLALCHEMY_DATABASE_URI = 'postgresql://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@postgresql:5432/' + POSTGRES_DB


SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')
