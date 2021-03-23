from flask_login import LoginManager

login = LoginManager()
#login.blueprint_login_views()
login.login_view = 'auth.login'

def init_app(app):
    login.init_app(app)