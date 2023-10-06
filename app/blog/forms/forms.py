from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, DateTimeField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_ckeditor import CKEditorField
from blog.database.models import User, Post, Category
from email_validator import validate_email

class UserAdminForm(FlaskForm):
    full_name = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('Endereço de Email', render_kw={"placeholder": "email@example.com"},validators=[DataRequired(), Email('Enter with a valid email address')])
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField(
        'Senha',
        validators=[
            DataRequired()
        ]
    )
    admin = BooleanField('Admin?', default=False)

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Endereço de email já cadastrado, por favor tente outro')

    def validate_username(self, username):
        user = User.query.filter_by(email=username.data).first()
        if user is not None:
            raise ValidationError('Nome de usuario já cadastrado, por favor tente outro')

class UserLogin(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": "email@example.com"},validators=[DataRequired(), Email('Enter with a valid email address')])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me', default=False)
    submit = SubmitField('Entrar')

class UserRegistrationForm(FlaskForm):

    full_name = StringField('Nome completo', validators=[DataRequired()])
    email = StringField('Endereço de Email', render_kw={"placeholder": "email@example.com"},validators=[DataRequired(), Email('Enter with a valid email address')])
    username = StringField('Nome de usuario', validators=[DataRequired()])
    password = PasswordField(
        'Senha',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Repetir senha', validators=[DataRequired(),
            EqualTo('password', message='As senhas devem ser iguais')])
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

def list_categories():
    return Category.query.all()

class PostAdminForm(FlaskForm):
    user = QuerySelectField('Author', query_factory=lambda: User.query.all(),validators=[DataRequired()])
    title = StringField('Titulo', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    abstract = TextAreaField('Resumo', validators=[DataRequired()])
    content = CKEditorField('Conteudo', validators=[DataRequired()])

    category = QuerySelectField('Categoria', query_factory=list_categories,validators=[DataRequired()])

class CreateNewPostForm(FlaskForm):

    title = StringField('Titulo', validators=[DataRequired()])
    abstract = TextAreaField('Resumo', validators=[DataRequired()])
    content = CKEditorField('Conteudo', validators=[DataRequired()])

    category = QuerySelectField('Categoria', query_factory=list_categories,validators=[DataRequired()])
    submit = SubmitField('Criar postagem')



class CreateNewCategory(FlaskForm):

    name = StringField('Nome da categoria', validators=[DataRequired()])
    submit = SubmitField('Criar categoria')
