#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 15:43
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : userdao_test.py
# @software: PyCharm

import unittest
from mapping.model_map import DBSession, Users


class UserDaoTest(unittest.TestCase):
    """
    UserDao测试类
    """

    def setUp(self):
        print('this is setUp...')

    def test_add(self):
        """
        测试增加user数据
        :return:
        """
        print('this is test_add...')
        session = DBSession()
        new_user = Users(name='zhoubin', email='test@example.com', passwd='1234567890', image='about:blank')
        session.add(new_user)
        session.commit()
        session.close()

    def tearDown(self):
        print('this is tearDown...')


if __name__ == '__main__':
    unittest.main()
