#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 22:49
# @Author  : Hanwei Zhu
# @File    : base_graph.py

import tensorflow as tf


class BaseGraph(object):
    def __init__(self, config):
        self.config = config
        self.build_graph()

    def build_graph(self):
        pass
