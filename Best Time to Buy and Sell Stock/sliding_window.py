class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # l = the day to buy
        # r = the day to sell

        # Brutal Force
        # Try every combination of l, r to find the maximum profit

        # But do we have to try every single pair?
        # If value at r < value at l
        # we can skip testing the values between l and r
        # For the values at indexes after r yield any profit if you buy at l, you will get more profit if you buy at r

        # Example
        # 
        # ..., 2, 3, 4, 1, 2, 3, ...
        # values at l = 2
        # values at r = 1 (i.e. the first time, value at r smaller than value at l)
        # values at r + 1, r + 2 = 3
        # you will always earn more if you buy stock at r
        # so we can skip examining the indexes between l and r. In this example, we skip value l + 1 (value = 3), l + 2 (value = 4)


        l, r, max_profit = 0, 0, 0

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            if prices[l] <= prices[r]:
                r += 1
            else:
                l = r
        
        return max_profit