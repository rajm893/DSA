class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        if not prices:
            return max_profit
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
