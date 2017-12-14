import orm
from models import User, Blog, Comment


async def test(loop, **kw):
    await orm.create_pool(loop, user='root', password='123456', db='awesome')
    u = User(name='test', email='test@test.com',
             password='11111', image='about:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
import asyncio
