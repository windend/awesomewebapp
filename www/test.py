import orm
from models import User, Blog, Comment


async def test():
    await orm.create_pool(loop, user='root', password='123456', db='awesome')
    u = User(name='test', email='test@test.com',
             password='11111', image='about:blank')
    await u.save()
    # await orm.destroy_pool()


for x in test():
    pass
