# 学习笔记 #

## LRU Cache ##

LRU 缓存机制可以通过哈希表+双向链表实现，用一个哈希表和一个双向链表维护所有在缓存中的键值对。

- 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。

- 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。

首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，即可在 O(1) 的时间内完成 get 或者 put 操作。

### LRU Cache Python代码 ###

    class LRUCache(object): 
    
    	def __init__(self, capacity): 
    		self.dic = collections.OrderedDict() 
    		self.remain = capacity
    
    	def get(self, key): 
    		if key not in self.dic: 
    			return -1 
    		v = self.dic.pop(key) 
    		self.dic[key] = v   # key as the newest one 
    		return v 
    
    	def put(self, key, value): 
    		if key in self.dic: 
    			self.dic.pop(key) 
    		else: 
    			if self.remain > 0: 
    				self.remain -= 1 
    			else:   # self.dic is full
    				self.dic.popitem(last=False) 
    		self.dic[key] = value

### Python版十大经典排序算法代码 ###

1、冒泡排序（Bubble Sort）

    def bubbleSort(arr):
    	n = len(arr)
    	for i in range(n):
    		for j in range(n - i - 1):
   				if arr[j] > arr[j + 1]:
    				arr[j], arr[j + 1] = arr[j + 1], arr[j]
    	return arr

2、选择排序（Selection Sort）

    def selectionSort(arr):
    	n = len(arr)
    	for i in range(n - 1):
        	minIndex = i
        	for j in range(i + 1, n):
            	if arr[j] < arr[minIndex]:  # 寻找最小数
                	minIndex = j            # 将最小数的索引保存
        	arr[i], arr[minIndex] = arr[minIndex], arr[i]
    	return arr

3、插入排序（Insertion Sort）

    def insertionSort(arr):
    	n = len(arr)
    	for i in range(1, n):
        	preIndex = i - 1
        	current = arr[i]    # 通过current中间变量传值，防止元素后移时覆盖数值
        	while preIndex >= 0 and arr[preIndex] > current:
            	arr[preIndex + 1] = arr[preIndex]   # 已排序元素大于新元素时，将该元素后移一位
            	preIndex -= 1   # 回退一步再进行比较
        	arr[preIndex + 1] = current
    	return arr

4、希尔排序（Shell Sort）

    def shellSort(arr):
    	n = len(arr)
    	gap = n // 2	# 设定初始步长
    	while gap > 0:
        	for j in range(gap, n):
				# 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            	while j >= gap and arr[j - gap] > arr[j - gap]:
                	arr[j - gap], arr[j] = arr[j], arr[j - gap]
                	j -= gap
        	gap = gap // 2		# 新步长
    	return arr

5、归并排序（Merge Sort）
    
    def mergeSort(arr):
    	n = len(arr)
    	# 当列表元素只有一个的时候，直接返回
    	if n < 2:
    		return arr
    	mid = n // 2	# 将列表分成更小的两个列表
    	left = arr[:mid]
    	right = arr[mid:]
    	# 递归分解，将更小的列表继续分解，直到达到最小规模，也就是只有一个元素,再对已经排序好的列表进行合并.
    	return merge(mergeSort(left), mergeSort(right))

    def merge(left, right):
    	"""合并两个已排序好的列表，产生一个新的已排序好的列表"""
    	res = []	# 新的已排序好的列表
    	# 对两个列表中的元素 两两对比。将最小的元素，放到res中。
    	while len(left) > 0 and len(right) > 0:
    		if left[0] <= right[0]:
    			res.append(left.pop(0))
    		else:
    			res.append(right.pop(0))
    	while len(left):
    		res.append(left.pop(0))
    	while len(right):
    		res.append(right.pop(0))
    	return res

6、快速排序（Quick Sort）
    
    def partition(arr, left, right):
    	# arr[] --> 排序数组
    	# low  --> 起始索引
    	# high  --> 结束索引
    	i = left - 1		# 最小元素索引
    	pivot = arr[right]
    
    	for j in range(left, right):
			# 当前元素小于或等于 pivot 
    		if arr[j] <= pivot:
    			i += 1
    			arr[i], arr[j] = arr[j], arr[i]
    	arr[i + 1], arr[right] = arr[right], arr[i + 1]
    	return i + 1
    
    def quickSort(arr, left, right):
    	if left < right:
    		pi = partition(arr, left, right)
    		quickSort(arr, left, pi - 1)
    		quickSort(arr, pi + 1, right)
    	return arr

7、堆排序（Heap Sort）

    def heapify(arr, n, i):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    	'''
    	给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    	父节点：(root-1)//2
    	左子节点：2*root + 1
    	右子节点：2*root + 2  即：左子节点 + 1
    	'''
    	left = 2 * i + 1
    	right = 2 * i + 2
    	larger = i
    	if left < n and arr[larger] < arr[left]:
    		larger = left
    	if right < n and arr[larger] < arr[right]:
    		larger = right
    	if larger != i:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
    		arr[i], arr[larger] = arr[larger], arr[i]
    	# 递归的对子树做调整
    	heapify(arr, n, larger)
    
    def heapSort(arr):# 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    	# build_max_heap(heap)
    	n = len(arr)
    	# 构造一个堆，将堆中所有数据重新排序
    	for i in range(n, -1, -1):  # 自底向上建堆
    		heapify(arr, n, i)
    	# 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆，一个个交换元素。
    	for i in range(n - 1, -1, -1):
    		arr[0], arr[i] = arr[i], arr[0]
    		heapify(arr, i, 0)
    	return arr

使用Python的heapq堆模块

    from heapq import heappush, heappop
    
    def heapSort(iterable):
    	h = []
    	for value in iterable:
    		heappush(h, value)
    	return [heappop(h) for i in range(len(h))]


8、计数排序（Counting Sort）

计数排序适合数据量大且数据范围小的数据排序，如对人的年龄进行排序，对考试成绩进行排序等。

    def countingSort(arr):
    	n = len(arr)
    	if n < 2:
        	return arr
    	maxNum = max(arr)
    	count = [0] * (maxNum + 1)  # 索引为0~maxNum
    	for num in arr:
        	count[num] += 1     # 索引计数
    	newArr = []
    	# 遍历计数列表，添加到新列表中完成排序
    	for i in range(len(count)):
        	for _ in range(count[i]):
            	newArr.append(i)
    	return newArr

9、桶排序（Bucket Sort）

排序需要占用很多额外的空间，对桶内数据进行排序，选择哪种排序算法对于性能的影响至关重要。桶排序适用的场景并不多，用得多一点的是基于桶排序思想的计数排序和基数排序。

    def bucketSort(arr):
    	minValue, maxValue = min(arr), max(arr)
    	bucketCount = (maxValue - minValue) // 3 + 1    # 分配三个桶
    	buckets = [[] for _ in range(int(bucketCount))]
    	for num in arr:
        	buckets[(num - minValue) // 3].append(num)
    	newArr = []
    	for i in buckets:
        	for j in sorted(i):
            	newArr.append(j)
    	return newArr

10、基数排序（Radix Sort）

    def radixSort(arr):
    	maxNum = max(arr)
    	place = 1
    	while maxNum > 10**place:
        	place += 1		# 求出arr中最大值的位数
    	for i in range(place):	# i 表示按数据的个位、十位进行分桶
        	buckets = [[] for _ in range(10)]		# 创建10个桶
        	for num in arr:
            	radix = num // (10**i) % 10		# radix 表示分桶时桶对应的基数
            	buckets[radix].append(num)
        	j = 0	# j 表示合并桶中的数据时，将数据赋值给待排序列表中索引 j 的位置
        	for k in range(10):
            	for num in buckets[k]:
                	arr[j] = num
                	j += 1
    	return arr

