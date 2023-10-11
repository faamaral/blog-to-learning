from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_required

from blog.forms.forms import CreateNewCategory
from blog.database.models import Category
from blog.database.db import data

categories = Blueprint('categories', __name__)

@categories.route('/category/create_new', methods=['GET', 'POST'])
@login_required
def create_new():
    form = CreateNewCategory()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        data.session.add(category)
        data.session.commit()
        flash("Categoria adicionada")
        return redirect(url_for('posts.post_create'))
    return render_template('tests/new_category.html', title='Criar categoria', form=form)