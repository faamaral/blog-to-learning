from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from flask_ckeditor import CKEditorField

class UserLogin(FlaskForm):
    email = EmailField('Endereço de email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha', validators.DataRequired())
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class UserRegistrationForm(FlaskForm):

    full_name = StringField('Nome completo', validators.DataRequired())
    email = EmailField('Endereço de Email', [validators.DataRequired(), validators.Email()])
    username = StringField('Nome de usuario', validators.DataRequired())
    password = PasswordField(
        'Senha',
        [
            validators.DataRequired,
            validators.EqualTo('confirm_password', message='As senhas devem conicidir')
        ]
    )
    confirm_password = PasswordField('Repeat Password')
    admin = BooleanField('Será administrador?', validators.DataRequired())


class CreateNewPostForm(FlaskForm):

    title = StringField('Titulo', validators.DataRequired())
    abstract = CKEditorField('Resumo', validators.DataRequired)
    content = ...