# -*- coding:utf-8 -*-
'''
购物车程序
    要求用户输入工资，然后打印购物菜单
    用户可以不断的购买商品，直到钱不够为止
    退出时格式化打印用户已购买的商品和剩余金额
'''
shoplist = ('Car price 100000', 'Coffee price 30', 'Bike price 700', 'Pen price 100', 'Computre price 8000', 'Paper price 10')
list_shop = []
flag = False

if __name__ == "__main__":
    
    print("输入工资够买商品，[q] 退出程序")
    input_content = int(raw_input("请输入工资："))
    balance = input_content
    
    while True:
        
        print("... list_shop begin ...")
        for item in shoplist:
            print(item)
        print("... list_shop end ...")
        
        shop_name = raw_input("请选择商品名称：")
        
        if shop_name == 'q' or shop_name == 'Q':
            print("Your has choose quit!")
            if len(list_shop) != 0:
                print("The cart has ....")
                for list_cart in list_shop:
                    print(list_cart)
            else:
                print("Your cart has not anythins !")
            break
        else:
            for each_list in shoplist:
                if shop_name.lower() in each_list.lower():
                    item_money = int(each_list.split(" ")[2:][0])
                    flag = True
                    break
                else:
                    flag = False
            
            if balance > item_money:
                balance = input_content - item_money
                print("Your has choose %s add shopping Cart, balance has %d" % (shop_name, balance))
                list_shop.append(shop_name)
            else:
                print("Your balance is not enough, you can't buy it.")
                break
        
        
        
        
        
        
        
        
        
        
        
        
        