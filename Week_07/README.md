# Week07 学习笔记 #

## Trie树 ##

#### 3个基本性质： ####

1. 根节点不包含字符，除根节点外每一个节点都只包含一个字符； 
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串； 
3. 每个节点的所有子节点包含的字符都不相同。

Trie的典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

#### Trie 树代码模板 ####
    
    # Python 
    class Trie(object):
      
    	def __init__(self): 
    		self.root = {} 
    		self.end_of_word = "#" 
     
    	def insert(self, word): 
    		node = self.root 
    		for char in word: 
    			node = node.setdefault(char, {}) 
    		node[self.end_of_word] = self.end_of_word 
     
    	def search(self, word): 
    		node = self.root 
    		for char in word: 
    			if char not in node: 
    				return False 
    			node = node[char] 
    		return self.end_of_word in node 
     
    	def startsWith(self, prefix): 
    		node = self.root 
    		for char in prefix: 
    			if char not in node: 
    				return False 
    			node = node[char] 
    		return True

## 并查集 ##

#### 重要思想 ####

用集合中的一个元素代表集合

#### Python代码模板 ####

    # Python 
	def init(p): 
		# for i = 0 .. n: p[i] = i; 
		p = [i for i in range(n)] 
	 
	def union(self, p, i, j): 
		p1 = self.parent(p, i) 
		p2 = self.parent(p, j) 
		p[p1] = p2 
	 
	def parent(self, p, i): 
		root = i 
		while p[root] != root: 
			root = p[root] 
		while p[i] != i:  	# 路径压缩
			x = i; i = p[i]; p[x] = root 
		return root

## 双向BFS ##

适用于知道起点和终点的状态下使用，从起点和终点两个方向开始进行搜索，可以大大提高单个bfs的搜索效率。

自行编写代码模板，非标准：

    #Python
    
    def BFS(graph, start, end):
    	visited = set()
    	start_queue = []
    	end_queue = []
    	start_queue.append([start])
    	end_queue.append([end])
    	
    	while start_queue and end_queue:
    		node1 = start_queue.pop()
    		visited.add(node1)
    		process(node1)
    		nodes1 = generate_related_nodes(node1)
    		start_queue.push(nodes1)
    		
    		node2 = end_queue.pop() 
    		visited.add(node2)
    		process(node2)
    		nodes2 = generate_related_nodes(node2)
    		end_queue.push(nodes2)
		

## 启发式搜索 ##

### 对比 ###

DFS、BFS ：根据搜索的顺序依次进行搜索，可以称为盲目搜索，搜索效率非常低。

A*：利用当前与问题有关的信息作为启发式信息，大大提高搜索效率，减少查找次数。

#### A*代码模板 ####

    # Python
    def AstarSearch(graph, start, end):
    	pq = collections.priority_queue() # 优先级 —> 估价函数
    	pq.append([start]) 
    	visited.add(start)
    	while pq: 
    		node = pq.pop() # can we add more intelligence here ?
    		visited.add(node)
    		process(node) 
    		nodes = generate_related_nodes(node) 
       		unvisited = [node for node in nodes if node not in visited]
    		pq.push(unvisited)
