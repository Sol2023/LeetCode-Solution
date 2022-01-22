class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left =0
        right =len(nums)-1
        
        while left<=right:
            middle=left+(right-left)//2
            potential = nums[middle]
            
            if potential > target:
                right = middle-1
            elif potential < target:
                left = middle+1
            else:
                for i in range(left,right+1):
                    if nums[i]==target:
                        if left<i and nums[left]!=nums[i]:
                            left =i
                        right=i
                return [left,right]
        return [-1,-1]
        