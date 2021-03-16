

from flask import Blueprint, render_template, send_from_directory, request, url_for


main = Blueprint('main', __name__)

@main.route('/', methods=['get'])
def index():
    user = {'username': 'Fabiano'}
    posts = [
        {
            'author': {'username': 'Fabis'},
            'body': 'its a test'
        },
        {
            'author': {'username': 'Untilit'},
            'body': 'its a test 2'
        }
    ]
    return render_template('tests/home.html', title='My blog', user=user, posts=posts)






