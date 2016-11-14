# -*- coding:utf-8 -*-
import MySQLdb
import sys

class TransferMoney(object):
    
    def __init__(self, conn):
        self.conn = conn;
        
    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print("check_acct_available:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %s 不存在" % acctid)
            
        finally:
            cursor.close()
        
    
    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            print("has_enough_money:" + sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号 %s 没有足够的钱" % acctid)
            
        finally:
            cursor.close()
    
    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print("reduce_money:" + sql)
            # 数据中改变的数据
            if cursor.rowcount != 1:
                raise Exception("账号 %s 减款失败" % acctid)
            
        finally:
            cursor.close()
    
    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print("add_money:" + sql)
            # 数据中改变的数据
            if cursor.rowcount != 1:
                raise Exception("账号 %s 加款失败" % acctid)
            
        finally:
            cursor.close()
    
    
        
    def transfer(self, sourece_acctid, target_acctid, money):
        try:
            # 检测转出账户是否存在
            self.check_acct_available(sourece_acctid)
            # 检测转入账户是否存在
            self.check_acct_available(target_acctid)
            # 检测转出账户是否有足够的钱
            self.has_enough_money(sourece_acctid, money)
            # 转出账户金额减少
            self.reduce_money(sourece_acctid, money)
            # 转入转户增加金额
            self.add_money(target_acctid, money)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        

if __name__ == "__main__":
    '''
    sourece_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]
    '''
    sourece_acctid = raw_input("输入转出的用户id:")
    target_acctid = raw_input("输入转入的用户id:")
    money = raw_input("输入需要转账金额:")
    
    conn = MySQLdb.Connect(
        host='127.0.0.1', 
        user='root', 
        passwd="", 
        port=3306, 
        db="imooc", 
        charset="utf8"
    )
    
    tr_money = TransferMoney(conn)
    
    try:
        tr_money.transfer(sourece_acctid, target_acctid, money)
    except Exception as e:
        print("出现问题" + str(e))
    finally:
        conn.close()