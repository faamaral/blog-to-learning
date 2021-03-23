

from flask import Blueprint, render_template, send_from_directory, request, url_for
from flask_login import current_user


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    user = {'username': current_user.full_name}
    posts = [
        {
            'author': current_user.full_name,
            'body': 'its a test'
        },
        {
            'author': {'username': 'Untilit'},
            'body': 'its a test 2'
        }
    ]
    return render_template('tests/home.html', title='My blog', posts=posts)






