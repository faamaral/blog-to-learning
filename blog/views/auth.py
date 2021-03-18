from flask import Blueprint, render_template, flash, redirect
from blog.forms.forms import UserLogin
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLogin()
    if form.validate_on_submit():
        flash('Login requisitado por {}, Lembrar de mim = {}'.format(form.email.data, form.remember_me.data))
        return redirect('/')
    return render_template('tests/login.html', title="Entrar", form=form)