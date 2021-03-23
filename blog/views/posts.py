from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from blog.database.models import Post
from blog.database.db import data
from blog.forms.forms import CreateNewPostForm

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/post/<id>/<slug>')
def post_detail(id, slug):
    post = Post.query.get_or_404(id=id)
    return render_template('')

@posts_bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def post_create():
    form = CreateNewPostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, user_id=current_user.id,abstract=form.abstract.data, content=form.content.data, category_id=form.category.data.id)
        data.session.add(post)
        data.session.commit()
        flash("Post Criado com sucesso")
        return redirect(url_for('main.index'))
    return render_template('tests/new_post.html', title="Crie um novo Post", form=form)
