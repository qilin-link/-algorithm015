#################################
# Leetcode 130. 被围绕的区域
#################################
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)

        if not board:
            return 0
        row = len(board)
        col = len(board[0])
        dummy = row * col   # 虚拟节点，所有不需要覆盖的都和它相连，最后再遍历一遍，没和dummy相连的就置为'X'。
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
                            if board[i + x][j + y] == 'O':
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board
if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    s = Solution()
    print(s.solve(board))
