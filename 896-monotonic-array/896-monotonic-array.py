class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isNonDecreasing = True
        isNonIncreasing = True
        
        for i in range(1,len(nums)):
            difference = nums[i] - nums[i-1]
            
            if difference >0:
                isNonIncreasing =False
            
            if difference <0:
                isNonDecreasing =False
                
        
        return isNonIncreasing or isNonDecreasing