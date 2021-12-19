class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        left=1
        for i in range(len(nums)):
            if i>0 and nums[i]!=nums[i-1]: 
                nums[left]=nums[i]
                left+=1
        return left