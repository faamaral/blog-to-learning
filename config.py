import os
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

'''DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = os.environ.get('SECRET_KEY')'''

class Config:

    SECRET_KEY = '1234teste'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dados.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    FLASK_ENV = 'development'
    FLASK_ADMIN_SWATCH = 'Flatly'
    # app.config['CKEDITOR_PKG_TYPE'] = 'basic'
    CKEDITOR_SERVER_LOCAL = False
    CKEDITOR_HEIGHT = 400
    CKEDITOR_WIDTH = 700
    UPLOADED_PATH = os.path.join(basedir, 'uploads')
    CKEDITOR_FILE_UPLOADER = 'uploads.upload'
    CKEDITOR_ENABLE_CSRF = True  # if you want to enable CSRF protect, uncomment this line

    # app.config['UPLOADED_PATH'] = 'blog/uploads'



