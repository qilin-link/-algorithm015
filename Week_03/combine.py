class Solution:
    def combine(self, n: int, k: int):
        ans = []
        if n == 0 or k == 0:
            return 
        def backtrace(tmp: list, index: int):
            # terminator
            if len(tmp) == k:
                ans.append(tmp[:])
                return ans
            # process
            for i in range(index, n + 1):
                tmp.append(i)
            # drill down
                backtrace(tmp, i + 1)
                tmp.pop()
        backtrace([], 1)
        return ans
if __name__ == "__main__":
    n = 4
    k = 2
    res = Solution().combine(n, k)
    print(res)


