# first thing that runs when Flask app is started
from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from config import Config


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
# from flask_cors import CORS
from helpers import JSONEncoder

# app instance to let Flask run
app = Flask(__name__)
# CORS(app)

# registering site blueprint to app
app.register_blueprint(site)
# registering auth blueprint to app
app.register_blueprint(auth)
# registering api blueprint to app
app.register_blueprint(api)

app.json_encoder = JSONEncoder

# grabbing config file for app to run
app.config.from_object(Config)

# initiate the db with the app and run login manager
# get app ready to upload and modify db tables using migrate
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
