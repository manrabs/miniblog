from flask import Flask

# The app variable below is defined as an instance of class Flask in the __init__.py script, which makes it a member of the app package
app = Flask(__name__)

# The app package below is defined by the app directory and the __init__.py script, and is referenced in the from app import routes statement.
from app import routes
