#######################
# Leetcode 547. 朋友圈
#######################
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        if n == 0: return 0
        p = [[0] for i in range(n)]
        def find(a):
            if p[a] != a: 
                p[a] = find(p[a])
            return p[a]
        def union(a, b):
            p[find(b)] = find(a)
            return find(b)
        for a in range(n):
            for b in range(a):
                if M[a][b]:
                    union(a, b)
        for i in range(n):
            find(i)
        return len(set(p))
if __name__ == "__main__":
    n = [["1", "1"," 0"],
         ["1", "1", "0"],
         ["0", "0", "1"]]
    S = Solution()
    print(S.findCircleNum(n))