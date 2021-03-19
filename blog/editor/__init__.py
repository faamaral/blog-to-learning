from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect

ckeditor = CKEditor()
csrf = CSRFProtect()

def init_app(app):
    ckeditor.init_app(app)
    csrf.init_app(app)