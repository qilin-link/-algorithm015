#######################
# Leetcode 647. 回文子串
#######################
from typing import List
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [[0] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1 
        return count

if __name__ == "__main__":
    n = "abc"
    S = Solution()
    print(S.countSubstrings(n))
