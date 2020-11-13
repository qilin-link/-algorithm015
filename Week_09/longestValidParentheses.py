#################################
# leetcode [32] 最长有效括号
#################################
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 0
        dp = [0 for _ in range(n)]
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0  and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

if __name__ == "__main__":
    s = "(()))())("
    res = Solution().longestValidParentheses(s)
    # print("最长有效括号= d%" % res)
    print(res)
