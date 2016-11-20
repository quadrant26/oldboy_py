# -*- coding:utf-8 -8-

# 设置标志位
def breakplay():
    while True:
        break_flag = raw_input('是否继续？(y/n)')
        if break_flag == 'y' or break_flag == 'n':
            return break_flag
        else:
            print("输入错误，请重新输入")
            
info_file = open('information.txt', 'r') # 只读文件的形式打开文件
# 读入员工信息, 生成一个列表
employee_info = info_file.readlines()
info_file.close()

break_flag = ''
print("欢迎来到员工信息查询系统")

while break_flag != 'n':
    while True:
        search_info = raw_input("请输入您需要查询的信息...")
        if len(search_info) > 2: # 判断输入字符的长度， 少于三个字符，需要重新输入
            break
        else:
            print("输入不合法，重新输入")
            
    count_number = 0
    search_info_list = []
    for i in employee_info:
        if i.count(search_info) > 0:
            search_info_list.append(i.replace(search_info, '\033[42;31;1m%s\033[0m' % search_info))
            count_number += i.count(search_info)
        
        if count_number > 0:
            print("一共查询到： \033[31; 1m %s \033[0m 条信息 ！" % count_number)
            for i in search_info_list:
                print(i)
            break_flag = breakplay()
        else:
            print("没有查询到您需要的信息")
            break_flag = breakplay()
        
    for i in range(2):
        print("感谢使用查询系统 %s 秒后， 系统退出" % (3-i))
    exit()