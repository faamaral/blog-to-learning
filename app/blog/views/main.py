

from flask import Blueprint, render_template, send_from_directory, request, url_for
from flask_login import current_user

from blog.database.models import Post


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    # user = current_user.full_name

    # posts = Post.query.order_by(Post.created.desc()).all()

    
    posts = [
        {
            'author': 'teste',
            'body': 'its a test'
        },
        {
            'author': 'Untilit',
            'body': 'its a test 2'
        }
    ]
    
    return render_template('index.html', title='My blog', posts=posts)






