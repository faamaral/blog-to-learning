import os
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = os.environ.get('SECRET_KEY')



