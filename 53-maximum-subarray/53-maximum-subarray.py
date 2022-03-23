class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = maxSum =nums[0]
        
        for num in nums[1:]:
            curSum = max(num, curSum+num)
            maxSum = max(curSum, maxSum)
        
        return maxSum
        
        
#         maxSum = -math.inf
        
#         for i in range(len(nums)):
#             currentSum = 0
#             for j in range(i,len(nums)):
#                 currentSum+=nums[j]
#                 maxSum = max(currentSum, maxSum)
        
#         return maxSum
        