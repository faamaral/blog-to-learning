

from flask import Blueprint, render_template, send_from_directory, request, url_for
from flask_login import current_user

from blog.database.models import Post, Category


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@main.route('/index', methods=['GET'])
def index():
    # user = current_user.full_name

    page = request.args.get('page', 1, type=int)

    categories = Category.query.all()

    posts = Post.query.order_by(Post.created.desc()).paginate(page=page, per_page=5, error_out=False)

    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    
    return render_template('index.html', title='My blog', posts=posts.items, categories=categories, next_url=next_url, prev_url=prev_url)






