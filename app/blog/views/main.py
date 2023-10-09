

from flask import Blueprint, render_template, send_from_directory, request, url_for
from flask_login import current_user

from blog.database.models import Post, Category


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET'])
def index():
    # user = current_user.full_name

    categories = Category.query.all()

    posts = Post.query.order_by(Post.created.desc()).all()

    # page = request.args.get('page')
    # if page and page.isdigit():
    #     page = int(page)
    # else:
    #     page = 1

    # pages = posts.paginate(page=page, per_page=5)

    
    # posts = [
    #     {
    #         'author': 'teste',
    #         'body': 'its a test'
    #     },
    #     {
    #         'author': 'Untilit',
    #         'body': 'its a test 2'
    #     }
    # ]
    
    return render_template('index.html', title='My blog', posts=posts, categories=categories)






