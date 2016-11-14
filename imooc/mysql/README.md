Python DB API 使用

1. python DB API 使用流程
	
	 开始  -> 创建 connect -> 获取 cursor
	 
	 数据库命令操作
	 
	 关闭 cursor 关闭 connect 结束
	 
2. mysql 开发环境
	
	python for mysql 2.7 https://sourceforge.net/projects/mysql-python/
	
3. connection 对象
	
	MySQLdb.Connect(参数)
		
		host 		string		mysql 服务器地址
		
		port 		number 		mysql 服务器端口号
		
		user		string		用户名
		
		passwd		string		密码
		
		db			string		数据库名称
		
		charset		string		连接编码

4. connection 方法

	cursor()			使用该连接创建并返回游标
	
	commit()			提交当前事务
	
	rollback()			回滚当前事务
	
	close()				关闭连接
	
5. cursor 游标对象
	
	execute(op[.args])			执行一个数据库查询和命令
	
	fetchone()						取得结果集的下一行
	
	fetchmany(size)				获取结果集的下几行
	
	feachall()						获取结果集中的剩下的所有行
	
	rowcount()						最近一次 execute 返回数据的行数或者影响行数
	
	close()							关闭游标对象
	
	fetch**()	利用 rownumber( 相当于指针 ) 返回数据
		
6. 数据库更新操作
	
	cursor.execute() 执行 i/u/d
	
	关闭自动 commit 设置 connecttion.autocommit(False)
	
	正常结束事务：		connection.commit()
	
	异常结束事务：		connection.rollback()
	
	出现异常
	
		否 ： 	使用 connection.commit() 提交
		
		是：		使用 connection.rollback() 回滚
