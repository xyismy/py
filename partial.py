#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

int2 = functools.partial(int,base=2)

print(int2('10000'))

print(__name__)