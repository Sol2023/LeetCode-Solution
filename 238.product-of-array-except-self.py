#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1,2,3,4
        # left: 1,1*1,2*1,3*2 ==  1,1,2,6
        # right:2*3*4,3*4,4,1 ==  24,12,4,1
        # result = 24,12,8,6
        l= len(nums)
        left = [1]*l
        right = [1]*l
        running_product=1
        res =[]
        for i in range(l):
            if i>0:
                running_product *= nums[i-1]
                left[i] = running_product
        
        
        
        running_product=1
        for i in range(l-1,-1,-1):
            if i<l-1:
                running_product *=nums[i+1]
                right[i] = running_product
            
        print(left, right)

        for j in range(l):
            res.append(left[j]*right[j])
        
        return res
        
# @lc code=end

