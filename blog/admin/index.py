from flask_login.utils import current_user
from flask_login import login_required
from flask_admin import expose, AdminIndexView
from flask import redirect, url_for, request



class IndexAdmin(AdminIndexView):
    @login_required
    def _handle_view(self, name, **kwargs):
        # the magic lives in the _handle_view function.
        # inside here, you can check if the user is authenticated, etc.

        super(IndexAdmin, self)._handle_view(name, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated()
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))