# 学习笔记 #

# 递归 #

## 代码模板 ##



    def recursion(level,param1,param2,...):
    	#recursion terminator	递归终结条件
    	if level > MAX_LEVEL:
    		process_result
    		return
    
    	#process logic in current level	处理当前层逻辑
    	process(level,data...)
    
    	#drill down	下探到下一层
    	self.recursion(level+1,p1,...)
    
    	#reverse the current level status if needed	清理当前层


## 思维要点： ##


1. 不要人肉进行递归（最大误区）


2. 找最近最简方法，将其拆解成可重复解决的问题（重复子问题）


3. 数学归纳法思维

# 分治 #

## 代码模板 ##


    def divide_conquer(problem, param1, param2,...):
    	# recursion terminator	问题已解决了
    	if problem is None:
    		print_result
    		return
    	# prepare data	处理当前层逻辑（把大问题如何分解成子问题）
    	data = prepare_data(problem)
    	subproblems = split_problem(problem, data)
    	# conquer subproblems 	调用该函数下探到下一层（解决更细节的子问题）
    	subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    	subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    	subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    	...
    	# process and generate the final result	（将结果组装起来返回）
    	result = process_result(subresult1, subresult2, subresult3, …)
       
    	# revert the current level states