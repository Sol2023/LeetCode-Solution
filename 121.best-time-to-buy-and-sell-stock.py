#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        temp_min= float('inf')

        for price in prices:
            temp_min = min(temp_min, price)

            temp_profit = price - temp_min
            max_profit = max(max_profit, temp_profit)
        
        return max_profit
        
# @lc code=end

