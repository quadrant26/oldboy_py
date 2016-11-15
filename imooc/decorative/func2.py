# -*- coding:utf-8 -*-

def func_150(val):
    passline = 90
    if val >= passline:
        print('%d pass' % val)
    else:
        print('failed')
        
def func_100(val):
    passline = 60
    if val >= passline:
        print('%d pass' % val)
    else:
        print('failed')
        
def set_passline(passline): # 60
    def cmp(val):
        if val >= passline:
            print('Pass')
        else:
            print('failed')

    return cmp

f_100 = set_passline(60) # 第一次调用 passline 为 60
print(type(f_100))
print(f_100.__closure__)
f_100(89)
f_100(59)
        
