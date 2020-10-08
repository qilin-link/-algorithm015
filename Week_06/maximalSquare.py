from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxSqr = maxSide * maxSide
        return maxSqr
if __name__ == "__main__":
    S = Solution()
    n = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    res = S.maximalSquare(n)
    print(res)
