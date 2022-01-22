class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        threeLargest = [None, None, None]
        nums = list(set(nums))
        
        for num in nums:
            self.updateLargest(threeLargest, num)
        
        return threeLargest[0] if threeLargest[0] is not None else threeLargest[2]
        
    def updateLargest(self, array, num):
        if array[2] is None or array[2]<= num:
            self.shiftAndUpdate(array, num, 2) 
        elif array[1] is None or array[1]<= num:
            self.shiftAndUpdate(array, num, 1)
        elif array[0] is None or array[0]<= num:
            self.shiftAndUpdate(array, num, 0)
    
    def shiftAndUpdate(self, array, num, idx):
        for i in range(idx+1):
            if i==idx:
                array[i]=num
            else:
                array[i]=array[i+1]