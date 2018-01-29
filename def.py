# -*- coding:utf-8 -*-

def my_test( data ):
    if len(data) > 2:
        print(data)
    else:
        print('no')

def my_one( str ):
    for name in str:
        print(name)

names = ['Michael', 'Bob', 'Tracy']

my_test(names)
my_one(names)

def my_tow():
    pass