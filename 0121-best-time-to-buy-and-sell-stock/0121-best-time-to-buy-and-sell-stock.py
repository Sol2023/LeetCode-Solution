class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # brute force
        # max_profit = 0

        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j]-prices[i])
        
        # return max_profit



        min_price = float(inf)
        max_profit = -float(inf)

        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price- min_price)
        
        return max_profit




        