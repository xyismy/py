# -*- coding:utf-8 -*-

import time, functools

#装饰器
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now(data,str,da):
#     print('2015-3-25')
#
# now('123','456','qwe')




def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call % s()' % func.__name__)
        return func(*args,**kw)
    return wrapper


@log
def metric(data):
    print(data)
    return data


metric('123')