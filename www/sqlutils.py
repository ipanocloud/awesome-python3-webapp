#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/1 23:45
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : sqlutils.py
# @software: PyCharm

import logging
import aiomysql
import asyncio

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def create_pool(loop, **kw):
    """
    创建mysql数据库连接池
    :param loop:
    :param kw:
    :return:
    """
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    """
    封装select查询语句
    :param sql: select查询sql
    :param args: 参数
    :param size: 查询条数
    :return:
    """
    logging(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs
