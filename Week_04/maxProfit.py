from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        tmp = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit
if __name__ == "__main__":
    S = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(S.maxProfit(prices))

