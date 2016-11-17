1. 文件处理模式
	
	a. 文件打开方式 
		
		r 以只读模式打开文件
		
		w 以只写模式打开文件
		
		a 以追加模式打开文件
		
		r+b 以读写模式打开
		
		w+b 以写读模式打开
		
		a+b 以追加及读模式打开
		
		
2. 字符串处理
	
	S.find(substring, [start [,end]]) #可指范围查找子串，返回索引值，否则返回-1  
	
	S.rfind(substring,[start [,end]]) #反向查找  
	
	S.index(substring,[start [,end]]) #同find，只是找不到产生ValueError异常  
	
	S.rindex(substring,[start [,end]])#同上反向查找  
	
	S.count(substring,[start [,end]]) #返回找到子串的个数  
	  
	S.lowercase()  
	
	S.capitalize()      #首字母大写  
	
	S.lower()           #转小写  
	
	S.upper()           #转大写  
	
	S.swapcase()        #大小写互换  
	  
	S.split(str, ' ')   #将string转list，以空格切分  
	
	S.join(list, ' ')   #将list转string，以空格连接  
	  
	处理字符串的内置函数  
	
	len(str)                #串长度  
	
	cmp("my friend", str)   #字符串比较。第一个大，返回1  
	
	max('abcxyz')           #寻找字符串中最大的字符  
	
	min('abcxyz')           #寻找字符串中最小的字符  

3. 列表的方法
	
	L.append(var)  	 #追加元素  
	
	L.insert(index,var)  
	
	L.pop(var)      	#返回最后一个元素，并从list中删除之  
	
	L.remove(var)   	#删除第一次出现的该元素  
	
	L.count(var)    	#该元素在列表中出现的个数  
	
	L.index(var)   	 #该元素的位置,无则抛异常   
	
	L.extend(list)  	#追加list，即合并list到L上  
	
	L.sort()       	 #排序  
	
	L.reverse()     	#倒序  
	
	a[1:]       		#片段操作符，用于子list的提取  
		[1,2]+[3,4] 	#为[1,2,3,4]。同extend()  
		[2]*4       		#为[2,2,2,2]  
	
	del L[1]   		 #删除指定下标的元素  
	
	del L[1:3]  	#删除指定下标范围的元素  
	
	list的复制  
	
		L1 = L     		 #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作
	
		L1 = L[:]  		 #生成L的一个COPY 
		
4. dict
	
	D.get(key, 0)       #同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常  
	
	D.has_key(key)      #有该键返回TRUE，否则FALSE  
	
	D.keys()           	 #返回字典键的列表  
	
	D.values()          #以列表的形式返回字典中的值，返回值的列表中可包含重复元素  
	
	D.items()           #将所有的字典项以列表方式返回，这些列表中的每一项都来自于(键,值),但是项在返回时并没有特殊的顺序           
	  
	D.update(dict2)     #增加合并字典  
	
	D.popitem()         #得到一个pair，并从字典中删除它。已空则抛异常  
	
	D.clear()          	 #清空字典，同del dict  
	
	D.copy()           	 #拷贝字典  
	
	D.cmp(dict1,dict2)  #比较字典，(优先级为元素个数、键大小、键值大小)  
	                    #第一个大返回1，小返回-1，一样返回0  
	              
	dictionary的复制  
	
	dict1 = dict        #别名  	
	
	dict2=dict.copy()   #克隆，即另一个拷贝。
	
		