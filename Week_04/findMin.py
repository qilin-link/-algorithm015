from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        #doundary
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[left]: return nums[left]

        #Binary search way
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            if nums[mid - 1] > nums[mid]: return nums[mid]
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    S = Solution()
    print(S.findMin(nums))