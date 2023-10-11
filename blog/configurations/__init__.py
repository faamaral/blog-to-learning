import os
from dotenv import load_dotenv

def init_app(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, './../../.env'))

    secret = os.urandom(24)

    app.config['FLASK_APP'] = os.environ.get('FLASK_APP') or './blog/app.py'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secret
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'dados.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG') or False
    app.config['FLASK_ENV'] = os.environ.get('FLASK_ENV') or 'production'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['CKEDITOR_PKG_TYPE'] = 'full'
    app.config['CKEDITOR_SERVER_LOCAL'] = False
    app.config['CKEDITOR_HEIGHT'] = 400
    app.config['CKEDITOR_WIDTH'] = 700
    app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
    app.config['CKEDITOR_FILE_UPLOADER'] = 'uploads.upload'
    app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line

    #app.config['UPLOADED_PATH'] = 'blog/uploads'
