class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        isSorted=False
        count=0
        while not isSorted:
            isSorted=True
            for i in range(len(nums)-1-count):
                if nums[i]>nums[i+1]:
                    self.swap(i,i+1, nums)
                    isSorted=False
            count+=1
        
        return nums
    
    def swap(self, num1, num2, array):
        array[num1], array[num2] = array[num2], array[num1]