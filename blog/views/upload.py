import os

from flask import Blueprint, render_template, send_from_directory, request, url_for, current_app
from flask_ckeditor import upload_fail, upload_success
from blog.editor import csrf

up = Blueprint('uploads', __name__)

@up.route('/files/<filename>')
@csrf.exempt
def uploaded_files(filename):
    path = current_app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)

@up.route('/upload', methods=['POST'])
@csrf.exempt
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join(current_app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploads.uploaded_files', filename=f.filename)
    return upload_success(url=url)
