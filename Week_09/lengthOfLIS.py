#################################
# leetcode [300] 最长上升子序列
#################################
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[i]

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution()
    print(s.lengthOfLIS(nums))
