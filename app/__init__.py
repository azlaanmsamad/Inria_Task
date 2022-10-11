import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
