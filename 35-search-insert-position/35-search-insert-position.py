class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right =len(nums)-1
        
        while left<=right:
            middle= left+ (right-left)//2
            potential = nums[middle]
            if potential == target:
                return middle
            elif potential > target:
                right = middle-1
            else:
                left = middle+1
        
        return left
        