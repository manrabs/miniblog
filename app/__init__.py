from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# The app variable below is defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# this ensures that a user not logged in tries to view a protected page gets redirected by Flask-Login automatically to the login form, and only redirect back to the page the user wanted to view after the login process is complete. the 'login' value is the function (or endpoint) name for the login view. i.e. the name you'd use in a url_for() call to get/redirect the URL.
login.login_view = 'login'

# The app package below is defined by the app directory and the __init__.py script, and is referenced in the from app import routes statement.
from app import routes, models
