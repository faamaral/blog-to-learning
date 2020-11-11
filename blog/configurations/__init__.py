
def init_app(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db-dev.sqlite'
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'
