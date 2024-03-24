class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        temp_sum=0
        
        max_sum=-float(inf)
        i=0
        
        
        while i<len(nums) :
            
            while i<k:
            
                temp_sum+=nums[i]
                i+=1
                
            # print(max_sum)
            
            max_sum = max(max_sum, temp_sum)
            
            if i<len(nums):
                temp_sum = temp_sum - nums[i-k] + nums[i]

                max_sum = max(max_sum, temp_sum)
            i+=1
            # print(max_sum)
        
        return max_sum/k
            
            
        