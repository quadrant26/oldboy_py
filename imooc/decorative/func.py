# -*- coding:utf-8 -*-

passline = 60

def func(val):
    # passline 在函数内部没有找到，则去全局对象查找
    # print( '%x'%id(val))
    if val >= passline:
        print('pass')
    else:
        print('failed')
        
    def is_fn():
        print(val)
        
    is_fn()
    
    return is_fn
        
f = func(80)
f() # is_fn

print(f.__closure__)