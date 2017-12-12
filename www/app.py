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


def index(request):
    return web.Response(body='<h1>Awesome country little hey jude</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '192.168.0.110', 9000)
    logging.info('server started at http://localhost:9000...')
    return srv


# @asyncio.coroutine
# def create_pool(loop, **kw):
#     logging.info('create database connection pool...')
#     global __pool
#     __pool = yield from aiomysql.create_pool(
#         host=kw.get('host', 'localhost'),
#         port=kw.get('port', 3306),
#         user=kw['user'],
#         password=kw['password'],
#         db=kw['db'],
#         charset=kw.get('charset', 'utf8'),
#         autocommit=kw.get('autocommit', True),
#         maxsize=kw.get('maxsize', 10),
#         minsize=kw.get('minsize', 1),
#         loop=loop
#     )


# @asyncio.coroutine
# def select(sql, args, size=None):
#     log(sql, args)
#     global __pool
#     with(yield from __pool) as conn:
#         cur = yield from conn.cursor(aiomysql.DictCursor)
#         yield from cur.excute(sql.replace('?', '%s'), args or())
#         if siz:
#             rs = yield from cur.fetchmany(size)
#         else:
#             rs = yield from cur.fetchall()
#         yield from cur.close()
#         logging.info('rows return:%s' % len(rs))
#         return rs


# @asyncio.coroutine
# def excute(sql, args):
#     log(sql)
#     with (yield from __pool) as conn:
#         try:
#             cur = yield from conn.cursor()
#             yield from cur.excute(sql.replace('?', '%s'), args)
#             affected = cur.rowcount
#             yield from cur.close()
#         except Exception as e:
#             raise
#         return affected


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
