from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField

class PostAdmin(ModelView):

    form_overrides = dict(content=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'
