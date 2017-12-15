import orm
import asyncio
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    u = User(name='test', email='test@test.com',
             password='11111', image='about:blank')
    await u.save()
# await orm.destroy_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
