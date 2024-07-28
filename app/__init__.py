from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# The app variable below is defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# The app package below is defined by the app directory and the __init__.py script, and is referenced in the from app import routes statement.
from app import routes, models
