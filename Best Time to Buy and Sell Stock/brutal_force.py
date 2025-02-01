class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brutal Force

        profit = 0
        if len(prices) < 2:
            return profit

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
               if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit