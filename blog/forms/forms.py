from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_ckeditor import CKEditorField
import email_validator

class UserLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email('Enter with a valid email address')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me', default=False)
    submit = SubmitField('Entrar')

class UserRegistrationForm(FlaskForm):

    full_name = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('Endereço de Email', validators=[DataRequired(), Email('Enter with a valid email address')])
    username = StringField('Nome de usuario', validators=[DataRequired()])
    password = PasswordField(
        'Senha',
        validators=[
            DataRequired(),
            EqualTo('confirm_password', message='As senhas devem conicidir')
        ]
    )
    confirm_password = PasswordField('Repeat Password')
    admin = BooleanField('Será administrador?', validators=[DataRequired()])


class CreateNewPostForm(FlaskForm):

    title = StringField('Titulo', validators=[DataRequired()])
    abstract = CKEditorField('Resumo', validators=[DataRequired()])
    content = CKEditorField('Conteudo', validators=[DataRequired()])
