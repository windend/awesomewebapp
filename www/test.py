import orm
from models import User, Blog, Comment


def test():
    yield from orm.create_pool(user='root', password='123456', database='awesome')

    u = User(name='test', email='test@test.com', password='11111', image='')

    yield from u.save()

for x in test():
    pass
