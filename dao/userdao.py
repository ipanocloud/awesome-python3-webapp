#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 15:28
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : userdao.py
# @software: PyCharm


from dao import Base, Column, String, DBSession


class User(Base):
    """
     user model orm mapping
    """
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
