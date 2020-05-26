#!/usr/local/bin python3
# -*- coding: utf-8 -*-
# @Project : aria2_web
# @File    : __init__.py.py
# @Author  : shangyameng@datagrand.com
# @Time    : 2020/5/23 23:50
# @desc:

from flask import current_app


class MyLogger(object):
    def info(self, message):
        return current_app.logger.info(message)

    def error(self, message):
        return current_app.logger.info(message)

    def debug(self, message):
        return current_app.logger.info(message)

    def warning(self, message):
        return current_app.logger.info(message)
