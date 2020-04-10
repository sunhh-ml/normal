# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/4/9 14:51
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : lxf_test.py
# @Software     : PyCharm
# @Project      : normal

from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()