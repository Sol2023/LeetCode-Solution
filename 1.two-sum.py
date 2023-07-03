#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)-1):
        #     for j in range(i,len(nums)):
        #         candidate = nums[i]+nums[j]
        #         if candidate == target:
        #             return [i,j]
        # return -1

        dit={}

        for i, num in enumerate(nums):
            potential = target - num 

            if potential in dit:
                return [dit[potential], i]
            else:
                dit[num]=i 
        
        return -1
        
# @lc code=end

