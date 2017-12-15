import orm
from models import User, Blog, Comment


<<<<<<< HEAD
async def test():
=======
async def test(loop, **kw):
>>>>>>> a4850b9209e0e9288ce50ef8ff17f4a30138b806
    await orm.create_pool(loop, user='root', password='123456', db='awesome')
    u = User(name='test', email='test@test.com',
             password='11111', image='about:blank')
    await u.save()
<<<<<<< HEAD
    # await orm.destroy_pool()


for x in test():
    pass
=======


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
import asyncio
>>>>>>> a4850b9209e0e9288ce50ef8ff17f4a30138b806
