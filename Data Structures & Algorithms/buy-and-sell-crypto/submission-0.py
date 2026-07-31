class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        current_profit, max_profit = 0, 0

        i, j = 0, 1

        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else: 
                current_profit = prices[j] - prices[i]
                max_profit = current_profit if current_profit > max_profit else max_profit
                j += 1

        return max_profit