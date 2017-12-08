#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 18:25
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : model_map.py
# @software: PyCharm

from mapping import Base, Column, String, DBSession, Float, Text, Boolean
import time
import uuid


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class Users(Base):
    __tablename__ = 'users'

    id = Column(String(50), primary_key=True, default=next_id)
    email = Column(String(50), unique=True)
    passwd = Column(String(50))
    admin = Column(Boolean, default=False)
    name = Column(String(50))
    image = Column(String(500))
    created_at = Column(Float, default=time.time)


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(String(50), primary_key=True, default=next_id)
    user_id = Column(String(50))
    user_name = Column(String(50))
    user_image = Column(String(500))
    name = Column(String(50))
    summary = Column(String(200))
    content = Column(Text)
    created_at = Column(Float, default=time.time)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(String(50), primary_key=True, default=next_id)
    blog_id = Column(String(50))
    user_id = Column(String(50))
    user_name = Column(String(50))
    user_image = Column(String(500))
    content = Column(Text)
    created_at = Column(Float, default=time.time)
