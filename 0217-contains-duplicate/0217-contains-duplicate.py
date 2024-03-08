class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # return len(nums)!=len(set(nums))
        
        nums = sorted(nums);
        
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]:
                return True
        
        return False