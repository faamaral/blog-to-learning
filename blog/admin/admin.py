from flask_admin import Admin

admin = Admin()

def init_app(app):

    admin.name = 'MY BLOG'
    admin.base_template = ...
