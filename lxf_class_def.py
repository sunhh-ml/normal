# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time         : 2020/4/7 21:30
# @Author       : Huanhuan sun
# @Email        : sun58454006@163.com
# @File         : lxf_class_def.py
# @Software     : PyCharm
# @Project      : normal


#  廖雪峰老师课程编的程序
#  利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    s1 = ''
    if s.isspace() or len(s) == 0:
        return s1
    a = s[0]
    b = s[-1]
    if a.isspace():
        if b.isspace():
            ss = s[1:-1]
        else:
            ss = s[1:]
    else:
        if b.isspace():
            ss = s[0:-1]
        else:
            return s
    return trim(ss)


def findmaxandmin(s):
    if len(s) == 0:
        return None, None
    smax = s[0]
    smin = s[0]
    for n in s:
        if n > smax:
            smax = n
        if n < smin:
            smin = n
    return smax, smin


#  请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in l1 if isinstance(x, str)]


# bb = []
# b = [x if isinstance(x, str) else bb for x in l1]

# 不是generator
# def triangels(n):
#     b = [1]
#     if n == 1:
#         return b
#     else:
#         b1 = triangels(n-1)
#         for m in range(n-1):
#             if m == 0:
#                 c = [1]
#             else:
#                 c.append(b1[m-1] + b1[m])
#         c.append(1)
#     return c

def triangels(n):
    b = [1]
    if n == 1:
        return b
    else:
        b1 = triangels(n-1)
        for m in range(n-1):
            if m == 0:
                c = [1]
            else:
                c.append(b1[m-1] + b1[m])
        c.append(1)
    return c

