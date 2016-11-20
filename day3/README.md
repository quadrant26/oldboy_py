1. 模块使用
	
	是否为主文件：__name__       if __name__ == ‘__main__’

	当前文件路径：__file__

	当前文件描述：__doc__
	
2. 函数式编程
	
	a. yield
	
		def AlexReadlines(): 
			seek = 0 
			while True: 
				with open('D:/temp.txt','r') as f: 											f.seek(seek) 
					data = f.readline() 
					if data: 
						seek = f.tell() 
						yield data 
					else: 
						return 
		for item in AlexReadlines(): 
			print item
			
	b. 三元运算
		result = 'gt' if 1>3 else 'lt‘
		print result
		
	
	c. lambda 表达式
		
		a = lambda x,y:x+y
		print a(4,10)
		
	d. 内置函数
		
		help()
		dir()
		vars()
		type()
		import temp
		reload(temp)
		id()

3. 常用模块
	
	random
		
		random.random()
		random.randint(1,2)
		random.randrange(1,10)
	
	md5加密
		
		import hashlib
		hash = hashlib.md5()
		hash.update('admin')
		print hash.hexdigest(
	
	pickle
	
	json

4. 正则表达式
	
	re.compile
	
	re.match	seach  findall
	
	group groups
	
5. 时间
	
	print time.mktime(time.localtime()) 
	print time.gmtime()    #可加时间戳参数
	print time.localtime() #可加时间戳参数
	print time.strptime('2014-11-11', '%Y-%m-%d') 
	print time.strftime('%Y-%m-%d') #默认当前时间
	print time.strftime('%Y-%m-%d',time.localtime()) #默认当前时间
	print time.asctime()
	print time.asctime(time.localtime())
	print time.ctime(time.time())
	
	

		
		
	