########################
# leetcode [52] N皇后 II
########################
class Solution:
    def totalNQueens(self, n):
        if n < 1:
            return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count
    def DFS(self, n, row, col, pie, na):
        # recursion terminator
        if row >= n:
            self.count += 1
            return 
        bits = (~(col | pie | na)) & ((1 << n) - 1)     # 得到当前所有的空位

        while bits:
            p = bits & - bits   # 取到最低位的1
            bits = bits & (bits - 1)    # 表示在p位置上放入皇后(清零最低位的1)
            self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))