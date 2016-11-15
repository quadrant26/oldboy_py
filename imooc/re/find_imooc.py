# -*- coding:utf-8 -*-
# 
def find_start_imooc(fname):
    f = open(fname, 'r')
    for line in f:
        if line.startswith('imooc'):
            print(line)
    
    f.close();
    
def find_in_imooc(fname):
    f = open(fname, 'r')
    for line in f:
        #if line.startswith('imooc') and line.endswith('imooc\n'):
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print(line)
    
    f.close();
            
find_start_imooc('imooc.txt')
        
a = "_value"

#  "_(下划线)" 或者 字母开头的 变量
print(a and (a[0] == "_" or 'a' <= a[0] <= 'z'))