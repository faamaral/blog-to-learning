

from flask import Blueprint, render_template, send_from_directory, request, url_for


main = Blueprint('main', __name__)

@main.route('/', methods=['get'])
def index():
    return render_template('index.html')






