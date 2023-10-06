import os

def init_app(app):
    basedir = os.path.abspath(os.path.dirname(__file__))

    app.config['SECRET_KEY'] = '1234teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    #app.config['CKEDITOR_PKG_TYPE'] = 'basic'
    app.config['CKEDITOR_SERVER_LOCAL'] = False
    app.config['CKEDITOR_HEIGHT'] = 400
    app.config['CKEDITOR_WIDTH'] = 700
    #app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
    app.config['CKEDITOR_FILE_UPLOADER'] = 'uploads.upload'
    app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line

    #app.config['UPLOADED_PATH'] = 'blog/uploads'
