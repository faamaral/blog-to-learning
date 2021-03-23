from flask import Blueprint

from blog.database.models import User, Post

author = Blueprint('author', __name__)

@author.route('author/<username>')
def author(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).all()


