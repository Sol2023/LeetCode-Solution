class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in reversed(range(len(digits))):
            digits[i]+=1
            digits[i] = digits[i]%10
            if digits[i]!=0:
                return digits
        
        return [1]+digits
        