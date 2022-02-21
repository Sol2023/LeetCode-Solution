class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        maxNumSoFar = nums[0]
        minNumSoFar = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, curr*maxNumSoFar, curr*minNumSoFar)
            temp_min = min(curr, curr*maxNumSoFar, curr*minNumSoFar)
            
            maxNumSoFar = temp_max
            minNumSoFar = temp_min
            
            result = max(result, maxNumSoFar)
        
        return result
        