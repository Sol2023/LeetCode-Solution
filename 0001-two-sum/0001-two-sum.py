class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # length = len(nums)

        # for i in range(length-1):
        #     for j in range(i+1,length):
        #         candidate = nums[i]+nums[j]

        #         if candidate == target:
        #             return [i,j]
        
        # return None
        

        dit = {}

        for i, num in enumerate(nums):
            candidate = target - nums[i]

            if candidate in dit:
                return [dit[candidate],i]
            else:
                dit[num] = i
        
        return None