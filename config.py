import os

#environment variable
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "myseckey12345"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" +  os.path.join(basedir, "my.db") 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    