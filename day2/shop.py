# -*- coding:utf-8 -*-
'''
购物车程序
    要求用户输入工资，然后打印购物菜单
    用户可以不断的购买商品，直到钱不够为止
    退出时格式化打印用户已购买的商品和剩余金额
'''
shoplist = ('Car price 100000', 'Coffee price 30', 'Bike price 700', 'Pen price 100', 'Computre price 8000', 'Paper price 10')
list_shop = []

print('Car' in shoplist)

if __name__ == "__main__":
    
    print("输入工资够买商品，[q] 退出程序")
    input_content = int(raw_input("请输入工资："))
    balance = input_content
    
    while True:
        # 商品列表
        print("... list_shop begin ...")
        for item in shoplist:
            print(item)
        print("... list_shop end ...")
        
        # 输入商品
        buy_some = raw_input("27 Please choose your buy something: ")
        # 判断是否选择退出
        if buy_some == 'q' or buy_some == "Q":
            print("Your has choose quit!")
            # 判断是否已经够买了商品
            if len(list_shop):
                print("Your shopping Cart has: ")
                for item_list in list_shop:
                    print('\t' + item_list)
            else:
                print("You don't have enough to buy anything. Your balance has %d !" % balance)
                
            break
        else:
            for each_shop in shoplist:
                # 判断所输入的商品是否在 列表中
                # error
                if buy_some.lower() in each_shop.lower():
                    item_money = int(each_shop.split(" ")[2:][0])
                    # 判断余额是否可以够买所输入的商品
                    if balance < item_money:
                        print("Your balance is not enough, you can't buy it.")
                        break
                    else:
                        balance = input_content - item_money
                        print("Your has choose %s add shopping Cart, balance has %d" % (buy_some, balance))
                        list_shop.append(each_shop)
                        break
                        
                else: # 商品不在列表中
                    print("55 The cart does not have the goods!")
                    break
        
        
