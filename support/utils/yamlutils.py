#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 11:52
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : yamlutils.py
# @software: PyCharm

import yaml
import os
import root


def readyaml():
    """
    读取固定yaml文件 转换成payton对象
    :return:
    """
    yamlfile = os.path.join(root.project_dir, 'conf', 'settings_dev.yaml').replace("\\", "/")
    return read_yaml_file(yamlfile)


def read_yaml_file(yamlfile):
    """
    从指定yaml文件中格式化数据(dict)
    :param yamlfile:
    :return:
    """
    with open(yamlfile) as stream:
        try:
            datamap = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return datamap


if __name__ == '__main__':
    readyaml()
