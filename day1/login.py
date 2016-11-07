# /usr/bin/env python
# -*- coding:utf-8 -*-

def login():
    
    user = "king"
    pws_user = "123456"
    count = 0
    
    with open("status.txt", 'r') as f:
        status = f.readline()
        if status != "lock":
            
            while True: 
                username = raw_input("请输入用户名：")
                pwd = raw_input("请输入密码：")
                
                if username == user and pws_user == pwd:
                    print("登陆成功，欢迎您， %s" % username)
                    break;
                else:
                    count = count + 1
                    print("用户名或密码错误，您已经输入了 %d：" % count)
                    if count >= 3:
                        print("您已经出错三次了，你的账号已被锁定！")
                        with open("status.txt", 'w') as f:
                            f.write("lock")
                        break
        else:
            print("由于连续出错三次，您的账号已经被锁定了！")
    
    
    

if __name__ == "__main__":
    login()
