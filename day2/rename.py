# -*- coding:utf-8 -*-

import os
import os.path

# 开发文件替换小程序

if __name__ == "__main__":
    
    file_name = raw_input("请输入需要改变的文件名：")
    if os.path.isfile(file_name):
        new_filename = raw_input("请输入修改后的文件名：")
        os.rename(file_name, new_filename)
        print("修改成功！")
    else:
        print("Your computre does not this < %s > file" % file_name)
    
    