from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_ckeditor import CKEditorField
from blog.database.models import User, Post
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
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Repetir senha', validators=[DataRequired(),
            EqualTo('password', message='As senhas devem conicidir')])
    admin = BooleanField('Admin?', default=False)
    submit = SubmitField('Cadastrar')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Endereço de email já cadastrado, por favor tente outro')

    def validate_username(self, username):
        user = User.query.filter_by(email=username.data).first()
        if user is not None:
            raise ValidationError('Nome de usuario já cadastrado, por favor tente outro')



class CreateNewPostForm(FlaskForm):

    title = StringField('Titulo', validators=[DataRequired()])
    abstract = CKEditorField('Resumo', validators=[DataRequired()])
    content = CKEditorField('Conteudo', validators=[DataRequired()])
