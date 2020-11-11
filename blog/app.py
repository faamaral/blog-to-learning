from flask import Flask
from blog.database import db
from blog import configurations
from blog import views

def create_app():
    app = Flask(__name__)

    configurations.init_app(app)
    #app.config.from_pyfile('config.py')
    db.init_app(app)
    views.init_app(app)

    return app