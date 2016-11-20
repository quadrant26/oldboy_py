# -*- coding : utf8 -*-

name = ['!', '#', '*', 'Eric', 'alex', 'jack', 'jack', 'a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6,2332,4,2,6,2]

pos_first = 0
for i in range(name.count(2)):
    new_list = name[pos_first:]
    pos_next = new_list.index(2) + 1

    print 'Find Position : ', pos_first + new_list.index(2), "Next :", pos_next
    pos_first += pos_next 
    