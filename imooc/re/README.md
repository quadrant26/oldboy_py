正则表达式

1. 基础查找

	a. 找到以 str 开头的方法
	
		content.startswith(str) 找到返回 True
	
	b. 找到以 str 结尾的方法
		
		content.endswith(str)
		
2. 正则表达式 
	
	import re
	
	pa = re.compile(r'pattern', flags)	(r 代表元字符串 ) flags = 'i/I,g/G,... (re.I)
	
	pa.match(string[, pos[, endpos]]) --> match object
	
	pa.match(...).group()  值保存在 group() 中
	
	span()			返回位置
	
	string			返回整体字符串
	
	re				返回字符串实例