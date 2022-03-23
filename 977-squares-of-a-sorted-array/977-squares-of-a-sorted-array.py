class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
#         for i in range(len(nums)):
#             nums[i]=nums[i]*nums[i]
        
#         nums.sort()
#         return nums
        l=len(nums)
        left = 0
        right = l-1
        result=[0]*l
        for i in range(l-1,-1,-1):
            if abs(nums[left])< abs(nums[right]):
                temp = nums[right]
                right-=1
            else:
                temp = nums[left]
                left+=1
            result[i]=temp*temp
        
        return result