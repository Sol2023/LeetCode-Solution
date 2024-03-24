class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left, zero_num, res = 0,0,0
        
        for i, num in enumerate(nums):
            
            if num==0:
                zero_num+=1
                
            if zero_num>k:
                
                if nums[left]==0: 
                    zero_num-=1
                
                left+=1
            
            if zero_num<=k:
                res = max(res, i-left+1)
            
        return res
                    
                    
        