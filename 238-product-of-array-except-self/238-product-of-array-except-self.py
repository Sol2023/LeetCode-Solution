class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = [None]*n
        
        left =1
        for i in range(len(nums)):
            if i>0: left=left*nums[i-1]
            res[i]=left
        
        right =1 
        j=n-1
        while j>=0:
            if j<n-1: right = right* nums[j+1]
            res[j]*=right
            j-=1
        
        return res