from flask_sqlalchemy import SQLAlchemy



data = SQLAlchemy()

def init_app(app):
    data.init_app(app)