class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -float(inf)
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum+=num
            running_sum = max(running_sum, num)

            max_sum = max(max_sum, running_sum)
        
        return max_sum

        