class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrace(nums,tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrace(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrace(nums, [])
        return res
if __name__ == "__main__":
    n = [1,2,3]
    res = Solution().permute(n)
    print(res)