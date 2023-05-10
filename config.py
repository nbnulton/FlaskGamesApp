# operates as a go-between for app and servers we're hosting on, 
# or talk to pc and interface between the app and command line/terminal
# need this before app is ran
import os

# importing functionality for loading .env file
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
    Set config variables for the flask app
    using Environment variables where available.
    Otherwise create the config variable if not done already
    ''' 
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'No Secret Key: Access Denied'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICAITONS = False


