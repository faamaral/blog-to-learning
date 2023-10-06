from flask_admin.contrib.sqla import ModelView
from blog.forms.forms import UserAdminForm


class UserAdmin(ModelView):
    form = UserAdminForm
    column_list = ('full_name', 'username', 'email', 'admin')