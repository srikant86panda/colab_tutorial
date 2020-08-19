#!/usr/bin/env python
# coding: utf-8

from utils.notebook_utils import is_jupyter

if is_jupyter():
    print('running on notebook')
else:
    print('not running on notebook')