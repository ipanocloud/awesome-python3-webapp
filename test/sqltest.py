#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/4 14:51
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : sqltest.py
# @software: PyCharm

import unittest
import asyncio
from www import sqlutils


class LearnSql(unittest.TestCase):
    """
    sqlutils单元测试
    """
    print('this is class tests\r\n')

    def setUp(self):
        # self.loop = asyncio.new_event_loop()
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        asyncio.set_event_loop(None)
        print('this is setup')

    def test_createpool(self):
        """
        测试创建MySQL连接池
        单元测试测试异步方法 https://stackoverflow.com/questions/23033939/how-to-test-python-3-4-asyncio-code
        :return:
        """
        print('test_createpool start....\r\n')
        # yield from sqlutils.create_pool(user='root', password='root', database='jt_cloudstitch')
        # self.loop.run_until_complete(
        #     asyncio.wait([sqlutils.create_pool(self.loop, user='root', password='root', database='jt_cloudstitch'),
        #                   sqlutils.select('select * from USER', '', 20)]))
        pool = self.loop.run_until_complete(
            sqlutils.create_pool(self.loop, user='root', password='root', database='jt_cloudstitch'))
        print(pool)
        print('test_createpool end....\r\n')

    def test_select(self):
        """
        测试SQL查询语句
        :return:
        """
        # rs = yield from sqlutils.select('select * from USER', '', 20)
        # self.loop.run_until_complete(sqlutils.select('select * from USER', '', 20))
        # self.loop.run_forever()

        # print('result' + rs)


if __name__ == '__main__':
    print('this is __name__')
    unittest.main()
