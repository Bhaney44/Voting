from distutils.debug import DEBUG
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False


class Debug(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.getenv('DATABASE_NAME')}"
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql:///{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASS')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"
    DEBUG = False