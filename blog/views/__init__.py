from blog.views.main import main
from blog.views.upload import up
from .auth import auth

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(up)
    app.register_blueprint(auth)