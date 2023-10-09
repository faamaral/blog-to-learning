from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from blog.database.models import Post, Category
from blog.database.db import data
from blog.forms.forms import CreateNewPostForm

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/post/<int:id>/<string:slug>', methods=['GET'])
def post_detail(id, slug):
    post = Post.query.filter_by(id=id).first()
    categories = Category.query.all()
    return render_template('post_detail.html', post=post, categories=categories)

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
    return render_template('post_detail.html', title="Crie um novo Post", form=form)

@posts_bp.route('/post/category/<int:id>', methods=['GET'])
def post_category(id):
    # Busca todos os posts por categoria
    category = Category.query.filter_by(id=id).first()
    posts = Post.query.filter_by(category_id=id).all()
    categories = Category.query.all()
    return render_template('post_category.html', posts=posts, category=category, categories=categories  )
