import os

from flask import Flask, send_from_directory, request, url_for
from flask_ckeditor import upload_fail, upload_success

from blog.database import db
from blog import configurations
from blog import views
from blog.admin import admin
from blog import editor
from blog.editor import csrf
from blog.login import login
from blog.database.models import User

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    configurations.init_app(app)
    app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
    #app.config.from_pyfile('config.py')
    db.init_app(app)
    editor.init_app(app)
    login.init_app(app)
    '''
    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    '''
    admin.init_app(app)
    views.init_app(app)





    return app