from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from flask_ckeditor import CKEditorField

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