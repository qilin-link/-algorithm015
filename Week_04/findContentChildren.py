#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0
        j = 0
        while i < len(g):
            while j < len(s):
                if s[j] >= g[i]:
                    res += 1
                    j += 1
                    break
                else:
                    j += 1
            i += 1
        return res
if __name__ == "__main__":
    S = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    print(S.findContentChildren(g,s))
