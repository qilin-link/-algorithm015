# 学习笔记 #

## 第19课 | 高级动态规划 ##

#### leetcode 63. 不同路径 II 的状态转移方程 ####

分析：

1、状态定义：
dp[i][j]表示走到格子 (i, j)的方法数。

2、状态转移：
如果网格 (i, j)上有障碍物，则 dp[i][j]值为 0，表示走到该格子的方法数为 0；
否则网格 (i, j)可以从网格 (i - 1, j)或者网格 (i, j - 1)走过来，因此走到该格子的方法数为走到网格 (i - 1, j)和网格 (i, j - 1)的方法数之和，即 dp[i, j] = dp[i - 1, j] + dp[i, j - 1]。

状态转移方程如下：
  
- (i,j)上无障碍物: dp[i][j] = dp[i-1][j] + dp[i][j-1]
- (i,j)上有障碍物: dp[i][j] = 0
    	
        dp[0][0] = 1
		# 第一列
        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
		# 第一行
        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
		# 状态转移方程计算终点路径数
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

## 第20课 | 字符串算法 ##

### Atoi 代码示例 ###

    # Python
    class Solution(object):
    	def myAtoi(self, s):
    		ls = list(s.strip())		# 去除两边空格
			if len(ls) == 0:			# 特判
				return 0
    
    		sign = -1 if ls[0] == '-' else 1		# 判断正副号
    		if ls[0] in ['-','+'] : del ls[0]
    		ret, i = 0, 0
    		while i < len(ls) and ls[i].isdigit() :
				# 数字字符转ASCII码十进制数字相减得到数字本身，ret*10：得到的数字进位后与新得到的数字相加
    			ret = ret*10 + ord(ls[i]) - ord('0')
    			i += 1
    		return max(-2**31, min(sign * ret,2**31-1))		# 越界判断

