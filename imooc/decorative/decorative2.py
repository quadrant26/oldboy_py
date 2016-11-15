# -*- coding:utf-8 -*-

def deco(func):
    def in_deco(x, y):
        print('in deco')
        func(x, y)
    print('call deco')
    return in_deco # 必须显示的返回
    
@deco
def bar(x, y):
    print('in bar', x+y)
print(type(bar))
bar(1, 3) # 如果不给 in_deco 不传递参数 会报错，缺少参数