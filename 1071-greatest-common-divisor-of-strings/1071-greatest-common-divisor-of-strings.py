class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        l = min(len(str1), len(str2))
        
        while l>0:
            
            if self.helper(l, str1, str2):
                return str1[:l]
            
            l-=1
        
        return ""
    
    
    def helper(self, l, str1, str2):
        
        if len(str1)%l>0 or len(str2)%l>0:
            return False
        
        base = str1[:l]
        
        n1, n2 = len(str1)//l, len(str2)//l
        
        return n1*base == str1 and n2*base==str2
            
            