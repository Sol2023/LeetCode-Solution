class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=nums[0]
        count=0
        for i in range(len(nums)):
            if(m==nums[i]): count+=1
            elif(count==0): m=nums[i]
            else: count-=1
        return m
        