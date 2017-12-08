#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 16:27
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : persondao_test.py
# @software: PyCharm

import unittest
from mapping.persondao import DBSession, Person


class PersonDaoTest(unittest.TestCase):
    def setUp(self):
        print('this is setUp')

    def test_add(self):
        print('this is test_add...')
        session = DBSession()
        new_user = Person(name='caobin', sex='女')
        session.add(new_user)
        session.commit()
        session.close()

    def tearDown(self):
        print('this is tearDown')


if __name__ == '__main__':
    unittest.main()
