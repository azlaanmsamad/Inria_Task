from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config, DevelopmentConfig, ProductionConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


# to avoid circular import
from flaskapp import routes
from flaskapp.models import Name

db.create_all()