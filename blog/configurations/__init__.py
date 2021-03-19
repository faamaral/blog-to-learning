import os
basedir = os.path.abspath(os.path.dirname(__file__))
def init_app(app):

    app.config['SECRET_KEY'] = '1234teste'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db-dev.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'
    app.config['FLASK_ADMIN_SWATCH'] = 'Flatly'
    app.config['CKEDITOR_FILE_UPLOADER'] = 'upload.upload'
    app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line
    app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')
    #app.config['UPLOADED_PATH'] = 'blog/uploads'
