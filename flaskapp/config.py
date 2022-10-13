import os
from dotenv import load_dotenv

load_dotenv()

# Find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    # Default settings
    FLASK_ENV = 'development'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # In memory DataBase
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL ')
    RESULT_BACKEND = os.getenv('RESULT_BACKEND')


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    # Postgres database URL has the form postgresql://username:password@hostname/database
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URl', default="sqlite:///" + os.path.join(basedir, 'prod.db'))