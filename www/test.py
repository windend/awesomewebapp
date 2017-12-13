# import orm
# from models import User, Blog, Comment


# async def test(loop, **kw):
#     await orm.create_pool(loop, user='root', password='123456', db='awesome')
#     u = User(name='test', email='test@test.com',
#              password='11111', image='about:blank')
#     await u.save()


# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.run_forever()
# import asyncio


# async def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = await asyncio.sleep(10)
#     print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host)
         for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
