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
from blog.database.models import User, Post, Category

from faker import Faker
from blog.database.db import data

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

app = create_app()

@app.cli.command()
def seed():
    faker = Faker('pt_BR')
    if not User.query.filter_by(username=os.environ.get('ADMIN_USERNAME'), email=os.environ.get('ADMIN_EMAIL')).exists():
        admin = User(full_name='Admin', username=os.environ.get('ADMIN_USERNAME'), email=os.environ.get('ADMIN_EMAIL'), password=os.environ.get('ADMIN_PASSWORD'), admin=True)
        data.session.add(admin)
        data.session.commit()
    for i in range(10):
        user = User(full_name=faker.name(), username=faker.user_name(), email=faker.email(), password=faker.password(), admin=False)
        data.session.add(user)
        data.session.commit()
    
    for i in range(8):
        category = Category(name=faker.word())
        data.session.add(category)
        data.session.commit()

    for i in range(20):
        post = Post(title=faker.sentence(), user_id=faker.pyint(1, 10), abstract=faker.paragraph(),content=faker.texts(), category_id=faker.pyint(1, 8))
        data.session.add(post)
        data.session.commit()