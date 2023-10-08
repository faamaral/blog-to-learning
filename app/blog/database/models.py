from slugify import slugify

from blog.database.db import data
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from blog.login import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(data.Model,UserMixin):
    __tablename__ = 'user'
    id = data.Column(data.Integer, primary_key=True)
    full_name = data.Column(data.String(50), nullable=False)
    email = data.Column(data.String(), unique=True, nullable=False)
    username = data.Column(data.String(20), index=True, unique=True, nullable=False)
    password = data.Column(data.String(), nullable=False)

    admin = data.Column(data.Boolean, default=False)

    def __init__(self, full_name, email, username, password, admin):
        self.full_name = full_name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.admin = admin

    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self) -> str:
        return f'<User> -> {self.username}'




class Category(data.Model):
    __tablename__ = 'category'

    id = data.Column(data.Integer, primary_key=True)
    name = data.Column(data.String(25), index=True, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Category> -> {self.name}'

class Post(data.Model):
    __tablename__ = 'post'

    id = data.Column(data.Integer, primary_key=True)

    title = data.Column(data.String, nullable=False)
    slug = data.Column(data.String, nullable=False)

    user_id = data.Column('author', data.Integer, data.ForeignKey('user.id'))
    user = data.relationship('User', foreign_keys=user_id)

    abstract = data.Column(data.Text, nullable=False)
    content = data.Column(data.Text, nullable=False)

    created = data.Column(data.DateTime, nullable=False, default=datetime.utcnow)
    last_edit = data.Column(data.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category_id = data.Column('category',data.Integer, data.ForeignKey('category.id'))
    category = data.relationship('Category', foreign_keys=category_id)

    def __init__(self, title, user_id, abstract, content, category_id):
        self.title=title
        self.slug = slugify(title)
        self.user_id=user_id
        self.abstract=abstract
        self.content=content
        self.category_id=category_id



