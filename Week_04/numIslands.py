from typing import List
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        lr, lc = len(grid), len(grid[0])    # 行和列的长度
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < lr and 0 <= y < lc and grid[x][y] == '1':
                self.dfs(grid, x, y)
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        if lr == 0: return 0
        lc = len(grid[0])   # 分开写，合着写会在上一步判断是报错越界
        num_islands = 0
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)
        return num_islands
if __name__ == "__main__":
    grid = [
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
           ]
    S = Solution()
    print(S.numIslands(grid))