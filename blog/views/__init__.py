from blog.views.main import main
from blog.views.upload import up
from blog.views.auth import auth
from blog.views.posts import posts_bp
from blog.views.categories import categories

def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(up)
    app.register_blueprint(posts_bp)
    app.register_blueprint(categories)
    app.register_blueprint(auth)
