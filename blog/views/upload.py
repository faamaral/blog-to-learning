import os

from flask import Blueprint, render_template, send_from_directory, request, url_for, current_app
from flask_ckeditor import upload_fail, upload_success

up = Blueprint('upload', __name__)

@up.route('/files/<filename>')
def uploaded_files(filename):
    path = current_app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

@up.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
    url = url_for('.uploaded_files', filename=f.filename)
    return upload_success(url=url)