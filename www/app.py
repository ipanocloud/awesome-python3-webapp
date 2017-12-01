#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/1 23:45
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : app.py
# @software: PyCharm

import logging
import asyncio
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    """
    响应自定义内容
    :param request:
    :return:
    """
    return web.Response(body=b'<h1>Hello World!</h1>', headers={'content-type': 'text/html'})


@asyncio.coroutine
def init(loop):
    """
    初始化web容器
    :param loop:
    :return:
    """
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
