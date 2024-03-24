class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        temp_hight=0
        res = 0
        
        for i, g in enumerate(gain):
            
            temp_hight+=g
            
            res = max(temp_hight, res)
        
        return res
        