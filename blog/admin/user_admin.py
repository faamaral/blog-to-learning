from flask_admin.contrib.sqla import ModelView
from blog.forms.forms import UserAdminForm
from flask_login import current_user


class UserAdmin(ModelView):
    form = UserAdminForm
    column_list = ('full_name', 'username', 'email', 'admin')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin