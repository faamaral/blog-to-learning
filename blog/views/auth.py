from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from blog.forms.forms import UserLogin, UserRegistrationForm
from blog.database.models import User
from blog.database.db import data


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = UserLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash("Email ou senha invalidos")
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
            return redirect(next_page)
    return render_template('tests/login.html', title="Entrar", form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(full_name=form.full_name.data, email=form.email.data,
                    username=form.username.data,password=form.password.data,
                    admin=form.admin.data)
        data.session.add(user)
        data.session.commit()
        flash('Parabens por ingressar no blog')
        return redirect(url_for('auth.login'))

    return render_template('tests/register.html', title='Cadastre-se', form=form)
