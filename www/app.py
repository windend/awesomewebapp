#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

import orm
from models import User, Blog, Comment


def index(request):
    return web.Response(body='<h1>Awesome halo1dd2321</h1>', content_type='text/html')


async def init(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    u = User(name='test', email='test@test.com',
             password='11111', image='about:blank')
    await u.save()
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    logging.info('server started at http://localhost:8000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
