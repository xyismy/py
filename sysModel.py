# -*- coding:utf-8 -*-

import sys

def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello')
    elif len(args) == 2:
        print('Words')
    else:
        print('Too')

if __name__ == '__main__':
    test()

print(__name__)