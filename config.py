import os

DEBUG = True
TESTING = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

POSTGRES_USER = 'characters_micro'
POSTGRES_PASSWORD = 'characters_micro'
POSTGRES_DB = 'characters_micro_db'
POSTGRES_SERVICE = 'postgres_characters'
SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVICE}:5432/{POSTGRES_DB}'

SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SWAGGER_DIR = os.path.join(BASE_DIR, 'api', 'swagger.yml')
