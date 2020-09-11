#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        s = ''
        def recur(left, right, s):
            #terminator
            if (left == n and right == n):
                res.append(s)
                return 
            if right > left:
                return
            #process#drill down
            if left < n:
                recur(left + 1, right, s + '(')
            if right < left:
                recur(left, right + 1, s + ')')
            #reverse states
        recur(0, 0, s)
        return res
# @lc code=end
if __name__ == "__main__":
    n = 3
    res = Solution().generateParenthesis(n)
    print(res)
