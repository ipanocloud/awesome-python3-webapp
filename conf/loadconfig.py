#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/5 13:46
# @author  : zhoubin
# @contact : zhoubin296@163.com
# @license : Copyright(C), ipanocloud
# @file    : loadconfig.py
# @software: PyCharm

import os
import root
import logging
from support.utils import yamlutils


def get_env_variable(var_name, default=False):
    """
    获取指定的环境变量value
    :param var_name:
    :param default:
    :return:
    """
    try:
        return os.environ[var_name]
    except KeyError as exc:
        print(exc)
        if default is not False:
            return 'dev'


def load_settings():
    """
    获取符合当前环境变量设置的配置文件(yaml)
    :return:
    """
    env = get_env_variable('PYTHON_ENV', True)
    logging.info('local env:' + env)
    yaml_file = os.path.join(root.project_dir, 'conf', 'settings_%s.yaml').replace("\\", "/") % env
    return yamlutils.read_yaml_file(yaml_file)
