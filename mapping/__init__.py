#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 15:26
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : __init__.py
# @software: PyCharm

from sqlalchemy import Column, String, create_engine, Integer, Boolean, Float, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf import load_config

Base = declarative_base()

yamlconfig = load_config.load_settings()
dbUrl = yamlconfig['dbUrl']
engine = create_engine(dbUrl)
DBSession = sessionmaker(bind=engine)
