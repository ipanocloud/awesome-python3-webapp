#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 16:22
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : persondao.py
# @software: PyCharm

from mapping import Base, Column, String, DBSession, Integer


class Person(Base):
    """
    person model mapping
    """
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20))
    sex = Column(String(20))
