# -*- coding:utf-8 -*-

import re

str1 = 'imooc python'

print(str1.find("11"))
print(str1.find('imooc'))

pa = re.compile(r'imooc')
print(pa)

help(pa.match)

ma1 = pa.match(str1)
print ma1.group()

print ma1.span()

print ma1.re

print ma1.string