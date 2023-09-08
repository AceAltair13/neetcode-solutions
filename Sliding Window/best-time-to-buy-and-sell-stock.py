class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0

        while j < len(prices):
            d = prices[j] - prices[i]
            max_profit = max(max_profit, d)
            if d < 0:
                i += 1
            else:
                j += 1

        return max_profit
