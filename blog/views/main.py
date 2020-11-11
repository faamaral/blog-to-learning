from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['get'])
def index():
    return 'HEllO World'

