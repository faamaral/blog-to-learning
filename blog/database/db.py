from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



data = SQLAlchemy()
migrate = Migrate()
def init_app(app):
    data.init_app(app)
    migrate.init_app(app, data)