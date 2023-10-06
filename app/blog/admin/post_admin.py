from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField
from blog.forms.forms import PostAdminForm

class PostAdmin(ModelView):
    form = PostAdminForm
    form_overrides = dict(content=CKEditorField)
    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'
