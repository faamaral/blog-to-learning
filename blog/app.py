from flask import Flask
from blog.database import db
from blog import configurations
from blog import views
from blog.admin import admin
from blog import editor
from blog.login import login
from blog.database.models import User


def create_app():
    app = Flask(__name__)

    configurations.init_app(app)
    #app.config.from_pyfile('config.py')
    db.init_app(app)
    editor.init_app(app)
    login.init_app(app)

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    admin.init_app(app)
    views.init_app(app)




    return app