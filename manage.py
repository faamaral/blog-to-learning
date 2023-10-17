from faker import Faker
from blog import app
from blog.models import User, Post, Category
from blog.database.db import data

app = app.create_app()

@manager.command
def seed():
    faker = Faker('pt_BR')
    admin = User(full_name='Admin', username='admin', email='admin@email.com', password='admin', admin=True)
    data.session.add(admin)
    data.session.commit()
    for i in range(10):
        user = User(full_name=faker.name(), username=faker.user_name(), email=faker.email(), password=faker.password(), admin=faker.pybool)
        data.session.add(user)
        data.session.commit()
    
    for i in range(8):
        category = Category(name=faker.word())
        data.session.add(category)
        data.session.commit()

    for i in range(20):
        post = Post(title=faker.sentence(), author_id=faker.pyint(1, 10), abstract=faker.paragraph,content=faker.text(), category_id=faker.pyint(1, 8))
        data.session.add(post)
        data.session.commit()
if __name__ == '__main__':
    manager.run()