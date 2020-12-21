from blog.database.db import data
from blog.database.models import Category, Post, User

def show_user():
    post = Post.query.filter_by().first()