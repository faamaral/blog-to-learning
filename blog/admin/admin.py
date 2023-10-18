from blog.admin.category_admin import CategoryAdmin
from flask_admin import Admin

from blog.admin.index import IndexAdmin
from blog.admin.user_admin import UserAdmin
from blog.database.models import Category,Post,User
from blog.database.db import data
from flask_admin.contrib.sqla import ModelView
from blog.admin.post_admin import PostAdmin


admin = Admin()

def init_app(app):


    admin.name = 'Techster'
    admin.template_mode = 'bootstrap4'
    admin.index_view = IndexAdmin()
    admin.add_view(UserAdmin(User,data.session))
    admin.add_view(PostAdmin(Post, data.session))
    admin.add_view(CategoryAdmin(Category,data.session))
    admin.init_app(app)

