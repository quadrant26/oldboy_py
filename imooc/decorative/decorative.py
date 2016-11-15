# -*- coding:utf-8 -*-

def dec(func):
    print('call dec')
    def in_dec(*arg): # my_sum
        print('in dec arg = ', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)
    print('return in_dec')
    return in_dec

@dec
def my_sum(*arg): # my_sum = in_dec
    print('in my sum')
    return sum(arg)

def my_average(*arg):
    return sum(arg)/len(arg)

print(my_sum(1, 2, 3, 4, 5))

# dec return in_dec -> my_sum
# my_sum = in_dec(*arg)
# my_sum = dec(my_sum)

# print(my_sum(1, 2, 3, 4, 5))

# print(my_average(1, 2, 3, 4, 5))
# print(my_average())